#ARG BASE_CONTAINER=ros:melodic


# https://hub.docker.com/repository/docker/ucsdets/scipy-ml-notebook/tags
#ARG BASE_CONTAINER=ucsdets/scipy-ml-notebook:2020.2-stable
ARG BASE_CONTAINER=ucsdets/datascience-notebook:2020.2-stable

FROM $BASE_CONTAINER

LABEL maintainer="UC San Diego ITS/ETS <ets-consult@ucsd.edu>"

# 2) change to root to install packages
USER root

RUN apt-get -y install vim
# 3) install packages
RUN pip install --no-cache-dir rospkg bagpy pandas
RUN pip3 install --no-cache-dir rospkg bagpy pandas

# 4) change back to notebook user
COPY /Docker/run_jupyter.sh /
RUN chmod 777 /run_jupyter.sh
USER $NB_UID