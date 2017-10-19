# posh
POSH: Parts Of Speech Heuristics

Build complex parts of speech rules with [Posh Syntax](https://github.com/brianray/posh-syntax) with support of Taxonomy and Ontologies. 

## Install

prerequisites:

* GCC and G+++ (4.7 > greater recommended)
* Python 2/3
* pip

### For Use

Choose one of (3) options.

(1) Conda:

```bash
conda install posh
```

(2) Pip:

```bash
pip install posh
```

(3) Source Code Install:

```bash
git clone --recursive https://github.com/brianray/posh.git
python setup.py install
```

### For Development

Recommended to use [docker_compose](https://docs.docker.com/compose/install/#install-compose)

Then :

```bash
 $ docker-compose up --build poshdev
```

Use `docker ps` to identify running process then connect look for example 'posh_poshdev_1'

```bash
docker attach posh_poshdev_1
```

Build the command line version
```bash
python setup.py makefile
make
```

You can ignore any 'Clock skew detected.' detections.

to debug
```bash
gdb ./posh_cli
(gdb) break main
(gdb) run
```

For the 'posh.core' extension:

```bash
python setup.py build 
```

environment (add to .bashrc):

```bash
export PYTHONPATH="./src:$PYTHONPATH"
```


## Setup/Tutorial

For quickstart:

```bash
ipython notebook notebooks/Tutorial.ipynb
```
ref [Tutorial](notebooks/Tutorial.ipynb)
