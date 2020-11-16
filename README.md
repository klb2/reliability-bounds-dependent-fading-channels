# Reliability Bounds for Dependent Fading Wireless Channels - Supplementary Material

This repository contains supplementary material to the paper "Reliability
Bounds for Dependent Fading Wireless Channels" (Karl-L. Besser and Eduard
Jorswieck, IEEE Transactions on Wireless Communications, vol. 19, no. 9, pp.
5833-5845, 2020, [arXiv:1909.01415 [cs.IT]](https://arxiv.org/abs/1909.01415),
[DOI:10.1109/TWC.2020.2997332](https://doi.org/10.1109/TWC.2020.2997332)).

The idea is to give an interactive version of the calculations to the reader
such that one can easily reproduce the plots presented in the paper as well as
changing parameters. One can also use this framework as a baseline and adjust
it to their own needs, e.g., for different channel models.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gl/klb2%2Freliability-bounds-dependent-fading-channels/master?filepath=Outage%20Capacity%20Rayleigh%20Channel.ipynb)

## File List
The following files are provided in this repository:

* [Outage Capacity Rayleigh
  Channel.ipynb](https://mybinder.org/v2/gl/klb2%2Freliability-bounds-dependent-fading-channels/master?filepath=Outage%20Capacity%20Rayleigh%20Channel.ipynb):
  This Jupyter notebook is the main notebook which contains the different
  curves for the epsilon-outage capacity for Rayleigh fading channels
* `best-case-epsilon-outage-rayleigh.ipynb` and
  `worst-case-epsilon-outage-rayleigh.ipynb`: Jupyter notbooks which contain
  more details about the best-case and worst-case epsilon-outage capacities for
  Rayleigh fading
* `best_case_rayleigh.py` and `worst_case_rayleigh.py`: Python modules that
  provide the functions for the best- and worst-case capacties
* `Exponential_Distribution.nb`: Mathematica notebook with derivations of the
  functions for the exponential distribution over the non-negative real
  numbers. This is used for the best-case capacity
* `Negative_Exponential_Distribution.nb`: Mathematica notebook with derivations
  of the functions for the exponential distribution over the non-positive real
  numbers. This is used for the worst-case capacity


## Usage
### Running it online
The easiest way is to use services like [Binder](https://mybinder.org/) to run
the notebook online. Simply navigate to
[https://mybinder.org/v2/gl/klb2%2Freliability-bounds-dependent-fading-channels/master?filepath=Outage%20Capacity%20Rayleigh%20Channel.ipynb](https://mybinder.org/v2/gl/klb2%2Freliability-bounds-dependent-fading-channels/master?filepath=Outage%20Capacity%20Rayleigh%20Channel.ipynb)
to run the notebook in your browser without setting everything up locally.

### Local Installation
If you want to run it locally on your machine, Python3 and Jupyter are needed.

Make sure you have [Python3](https://www.python.org/downloads/) installed on
your computer.
You can then install the required packages (including Jupyter) by running
```
pip3 install -r requirements.txt
jupyter nbextension enable --py widgetsnbextension
```
This will install all the needed packages which are listed in the requirements 
file. The second line enables the interactive controls in the Jupyter
notebooks.

Finally, you can run the Jupyter notebooks with
```
jupyter notebook 'Outage Capacity Rayleigh Channel.ipynb'
```

The present code was developed and tested with the following versions:
- Python 3.8
- Jupyter 1.0
- numpy 1.18
- scipy 1.4
- ipympl 0.5
- matplotlib 3.3



## Acknowledgements
This research was supported in part by the Deutsche Forschungsgemeinschaft
(DFG) under grant JO 801/23-1.


## License and Referencing
This program is licensed under the GPLv3 license. If you in any way use this
code for research that results in publications, please cite our original
article listed above.

You can use the following BibTeX entry
```
@article{Besser2020,
  doi = {10.1109/twc.2020.2997332},
  year = {2020},
  month = {9},
  publisher = {Institute of Electrical and Electronics Engineers ({IEEE})},
  volume = {19},
  number = {9},
  pages = {5833--5845},
  author = {Karl-Ludwig Besser and Eduard A. Jorswieck},
  title = {Reliability Bounds for Dependent Fading Wireless Channels},
  journal = {{IEEE} Transactions on Wireless Communications}
}
```
