# Reliable Communications Over Dependent Fading Wireless Channels - Supplementary Material

This repository contains supplementary material to the paper "Reliable
Communications Over Dependent Fading Wireless Channels" (Karl-L. Besser, Eduard
Jorswieck, 2019).

The idea is to give an interactive version of the calculations to the reader
such that one can easily reproduce the plots presented in the paper as well as
changing parameters. One can also use this framework as a baseline and adjust
it to their own needs, e.g., for different channel models.

## Usage
### Installation
Python3 and Jupyter notebooks are used for the implementation.  
If you want to run the files locally, make sure you have 
[Python3](https://www.python.org/downloads/) installed on your computer.

You can install the requires packages (including Jupyter) by running
```
pip3 install -r requirements.txt
```
This will install all the needed packages which are listed in the requirements 
file.

### Running the Notebooks
It is recommended to run the Jupyter notebooks since they provide interactive
plots.
To do this, simply run the following command
```
jupyter notebook 'Outage Capacity Rayleigh Channel.ipynb'
```

### Running it online
Alternatively, you can use services like [Binder](https://mybinder.org/) to run
the notebook online. Simply navigate to
[https://mybinder.org/v2/gl/klb2%2Foutage-dependent-fading-channels/master?filepath=Outage%20Capacity%20Rayleigh%20Channel.ipynb](https://mybinder.org/v2/gl/klb2%2Foutage-dependent-fading-channels/master?filepath=Outage%20Capacity%20Rayleigh%20Channel.ipynb)
to run the notebook in your browser without setting everything up locally.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gl/klb2%2Foutage-dependent-fading-channels/master?filepath=Outage%20Capacity%20Rayleigh%20Channel.ipynb)

