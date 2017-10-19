#!/bin/bash



jupyter notebook --no-browser --allow-root &

# from https://github.com/sequenceiq/hadoop-docker/blob/master/bootstrap.sh

if [[ $1 == "-d" ]]; then
  while true; do sleep 1000; done
fi

if [[ $1 == "-bash" ]]; then
  /bin/bash
fi