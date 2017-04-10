#!/bin/sh
cd /usr/bin/anaconda/bin/
export PATH=/usr/bin/anaconda/bin:$PATH
conda update matplotlib
conda install bokeh
