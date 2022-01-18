#import libraries required
import numpy as np
import random

import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import norm
from scipy.stats import poisson
from scipy.stats import binom

def sample_distribution_func(samples, distribution, mean=0, sd=1, mu=3, n=10, p=0.5):
    """This function will draw random numbers from a given distribution (Normal, Poisson, Binomial).
        
        It takes one argument for the number of samples and a second argument which specifies the
        distribution (Normal, Poisson or Binomial). 
        
        The function can also handle additional parameters depending on the distribution chosen"""
    
    f_sampled_distribution = np.zeros(shape=[0, 1])
    
    if distribution == "Normal":
        f_sampled_distribution = norm.rvs(size=samples, loc=mean, scale=sd)
        print (samples, "samples of a", distribution, "distribution with parameter values of mean =", mean, "and sd =", sd)
        return f_sampled_distribution
    elif distribution == "Poisson":
        f_sampled_distribution = poisson.rvs(size=samples, mu=mu)
        print (samples, "samples of a", distribution, "distribution with a parameter value of mu =", mu)
        return f_sampled_distribution
    elif distribution == "Binomial":
        f_sampled_distribution = binom.rvs(size=samples, n=n, p=p)
        print (samples, "samples of a", distribution, "distribution with parameter values of n =", n, "and p =", p)
        return f_sampled_distribution
    else:
        print('ERROR!:', distribution, "distribution is not defined within function")
        return f_sampled_distribution