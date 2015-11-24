# posh
POSH: Parts Of Speech Heuristics


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

Check out the code:

```bash
git clone --recursive https://github.com/brianray/posh.git
```

Build the posh_cli:

```bash
pip install bottle
python setup.py makefile
make
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
