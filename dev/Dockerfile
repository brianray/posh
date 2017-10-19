FROM continuumio/anaconda3

RUN conda update --yes conda
RUN conda update --yes --all

RUN apt-get update 
RUN apt-get -y install gcc
RUN apt-get -y install g++
RUN apt-get -y install make
RUN apt-get -y install gdb
Run apt-get -y install vim  # handy

ADD requirementsDEV.txt /etc/requirementsDEV.txt 
RUN pip install -r /etc/requirementsDEV.txt 
RUN pip install future

## from https://hub.docker.com/r/jupyter/notebook/~/dockerfile/

# Add a notebook profile.
RUN mkdir -p -m 700 /root/.jupyter/ && \
    echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py

ADD bootstrap.sh /etc/bootstrap.sh
RUN chown root:root /etc/bootstrap.sh
RUN chmod 700 /etc/bootstrap.sh

CMD ["/etc/bootstrap.sh", "-d"]

EXPOSE 8888:8888