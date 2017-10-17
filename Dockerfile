FROM continuumio/anaconda3

RUN conda update --yes conda
RUN conda update --yes --all

RUN apt-get update 
RUN apt-get -y install gcc
RUN apt-get -y install g++
RUN apt-get -y install make
Run apt-get -y install vim  # handy


RUN mkdir /shared
WORKDIR /shared
RUN git clone --branch dev --recursive https://github.com/brianray/posh.git
WORKDIR posh
RUN pip install -r requirementsDEV.txt
RUN pip install future
RUN python3 setup.py makefile
RUN python3 setup.py build 
RUN make

VOLUME /shared
WORKDIR /shared/posh/notebooks


## from https://hub.docker.com/r/jupyter/notebook/~/dockerfile/

# Add a notebook profile.
RUN mkdir -p -m 700 /root/.jupyter/ && \
    echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py

EXPOSE 8888

ENTRYPOINT ["tini", "--"]
CMD ["jupyter", "notebook", "--no-browser", "--allow-root"]