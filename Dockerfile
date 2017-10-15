FROM continuumio/anaconda

RUN apt-get update
RUN apt-get -y install gcc 
RUN apk add --no-cache \
    g++ \
    py-future \
    gdb \
    make

VOLUME /shared
WORKDIR /shared

RUN cd /shared
RUN git clone --branch dev --recursive https://github.com/brianray/posh.git
RUN pip install -r requirementsDEV.txt
RUN python setup.py makefile
RUN python setup.py build 
RUN make

## from https://hub.docker.com/r/jupyter/notebook/~/dockerfile/

# Add a notebook profile.
RUN mkdir -p -m 700 /root/.jupyter/ && \
    echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py

EXPOSE 8888

ENTRYPOINT ["tini", "--"]
CMD ["jupyter", "notebook", "--no-browser", "--allow-root"]