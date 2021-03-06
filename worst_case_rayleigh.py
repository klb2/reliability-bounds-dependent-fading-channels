"""Calculations of the worst case for dependent Rayleigh fading channels.

This module contains different functions to calculate the worst-case/lower
bound on the outage capacity for dependent Rayleigh fading channels.


Copyright (C) 2020 Karl-Ludwig Besser

This program is used in the article:
Karl-Ludwig Besser and Eduard Jorswieck, "Reliability Bounds for Dependent
Fading Wireless Channels", IEEE Transactions on Wireless Communications, 2020,
DOI:10.1109/TWC.2020.2997332.

License:
This program is licensed under the GPLv3 license. If you in any way use this
code for research that results in publications, please cite our original
article listed above.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.
See the GNU General Public License for more details.

Author: Karl-Ludwig Besser, Technische Universität Braunschweig
"""
__author__ = "Karl-Ludwig Besser"
__copyright__ = "Copyright (C) 2019-2020 Karl-Ludwig Besser"
__credits__ = ["Karl-Ludwig Besser", "Eduard A. Jorswieck"]
__license__ = "GPLv3"
__version__ = "1.0"

import numpy as np
from scipy import optimize

#np.seterr(all='raise')


# Definitions of f_{-}, F_{-}, G_{-}, H_{-}
def pdf(x):
    return np.exp(x)

def cdf(x):
    return np.exp(x)

def inv_cdf(x):
    return np.log(x)

def H(x, n, a):
    return inv_cdf(a+x) + (n-1)*inv_cdf(1-(n-1)*x)

def T(x, n, a):  # Integral of H
    return -n*x + (a+x)*np.log(a+x) + ((n-1)*x-1)*np.log(1-(n-1)*x)

def psi(a):  # Conditional expectation
    if a == 0:
        return -1
    if a == 1:
        return 0
    else:
        return (a-a*np.log(a)-1)/(1-a)


def lhs_cmin(c, n, a):
    if a+c == 0:
        return 0
    else:
        return (a-1) + n*c - (a+c)*np.log(a+c) - ((n-1)*c-1)*np.log(1-(n-1)*c)

def rhs_cmin(c, n, a):
    return ((1-a)/n-c)*H(c, n, a)

def diff_cmin(c, n, a):
    return lhs_cmin(c, n, a) - rhs_cmin(c, n, a)


def determine_cmin(n, a):
    if (a > 0) and (diff_cmin(0, n, a) < 0):
        return 0
    _eps = np.finfo(float).eps
    x0 = ((1-a)/n+_eps)/2
    bracket = [0+_eps, (1-a)/(n*(n-1))]
    try:
        solution = optimize.root_scalar(diff_cmin, args=(n, a), x0=x0,
                                        bracket=bracket)
    except ValueError as e:
        print("Error during root solving for n={:d}, a={:.2f}: {}".format(n, a, e))
        return 1
    #print(solution)
    return solution.root

def phi(a, n, cmin=None):
    if cmin is None:
        cmin = determine_cmin(n, a)
    if cmin > 0:
        _phi = H(0, n, a)
    elif cmin == 0:
        _phi = n*psi(a)
    else:
        raise ValueError("cmin must not be negative!")
    return _phi


def worst_case_rate(eps, snr, n):
    return np.log2(1-snr*phi(1-eps, n))
