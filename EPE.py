'EPE and effective EPE for Normal Distribution'

import pylab
import numpy as np
from scipy.stats import norm
import math

mu = 0.0
sigma = 0.1


def normcdf(x, mu, sigma):
    t = x-mu
    y = 0.5*math.erfcc(-t/(sigma*math.sqrt(2.0)))
    if y>1.0:
        y = 1.0
    return y


def normpdf(x, mu, sigma):
    u = (x-mu)/abs(sigma)
    y = (1/(math.sqrt(2*math.pi)*abs(sigma)))*math.exp(-u*u/2)
    return y


def normdist(x, mu, sigma, f):
    if f:
        y = normcdf(x,mu,sigma)/100.0
    else:
        y = normpdf(x,mu,sigma)/100.0
    return y


x = np.arange(-0.4, 0.4, 0.01)
y = norm.pdf(x, loc=mu, scale=sigma)

pfe = mu + norm.ppf(0.99)*sigma
print 'PFE %s' % pfe

ee = mu * norm.cdf(mu/sigma, loc=mu, scale=sigma) + sigma * normdist(mu/sigma, mu, sigma, False)
print 'EE %s' % ee

pylab.plot(x, y)
pylab.axvline(mu, linestyle='--', color='b')
pylab.axvline(ee, color='m')
pylab.axvline(pfe, color='r')
pylab.show()
