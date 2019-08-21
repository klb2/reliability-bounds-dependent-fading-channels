import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from matplotlib import widgets

#np.seterr(all='raise')

def pdf(x):
    return np.exp(-x)

def cdf(x):
    return 1-np.exp(-x)

def inv_cdf(x):
    x = np.minimum(x, 1)
    return -np.log(1-x)

def H(x, n, a):
    return (n-1)*inv_cdf(a+(n-1)*x) + inv_cdf(1-x)

def T(x, n, a):
    return n*x - x*np.log(x) + (1-a+x-n*x)*np.log(1-a+x-n*x)

def psi(a):
    if a == 1:
        return np.inf
    return 1 - np.log(1-a)


def lhs_cmin(c, n, a):
    if c == 0:
        return (-1 + a)*(-1 + np.log(1-a))
    return (1-a)-(c*n - c*np.log(c) + (1-a+c-c*n)*np.log(1-a+c-c*n))

def rhs_cmin(c, n, a):
    return ((1-a)/n-c)*H(c, n, a)

def diff_cmin(c, n, a):
    return lhs_cmin(c, n, a) - rhs_cmin(c, n, a)


def determine_cmin(n, a):
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
        _phi = H(cmin, n, a)
    elif cmin == 0:
        _phi = n*psi(a)
    else:
        raise ValueError("cmin must not be negative!")
    return _phi
    

def best_case_rate(eps, snr, n):
    return np.log2(1.+snr*phi(eps, n))
