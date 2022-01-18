import numpy as np
import random
from scipy.stats import norm
from scipy.stats import poisson
from scipy.stats import binom

class SampleDistributionClass:
    """This class will draw random numbers from a given distribution (Normal, Poisson, Binomial).
        
        It takes one argument for the number of samples and a second argument which specifies the
        distribution (Normal, Poisson or Binomial). 
        
        The class can also handle additional parameters depending on the distribution chosen"""

    # Initializer / Instance attributes
    def __init__(self, samples=10000, distribution='Normal'):
        self.samples = samples
        self.distribution = distribution
        print ("----------------------------",
               "{} samples of a {} distribution selected".format(self.samples, self.distribution),
               "----------------------------", 
               sep="\n")
    
    # instance draw method
    def draw(self, mean=0, sd=1, mu=3, n=10, p=0.5):
        self.mean = mean
        self.sd = sd
        self.mu = mu
        self.n = n     
        self.p = p
        
        self.cls_sampled_distribution = np.zeros(shape=[self.samples, 1])

        if self.distribution == "Normal":
            self.cls_sampled_distribution = norm.rvs(size=self.samples, loc=self.mean, scale=self.sd)
            print ("----------------------------",
                   "Normal distribution parameters: mean = {}; standard deviation = {}".format(self.mean, self.sd),
                   "----------------------------", 
                   sep="\n")
            return self.cls_sampled_distribution
        
        elif self.distribution == "Poisson":
            self.cls_sampled_distribution = poisson.rvs(size=self.samples, mu=self.mu)
            print ("----------------------------",
                   "Poisson distribution parameter: rate = {}".format(self.mu),
                   "----------------------------",
                   sep="\n")
            return self.cls_sampled_distribution
        
        elif self.distribution == "Binomial":
            self.cls_sampled_distribution = binom.rvs(size=self.samples, n=self.n, p=self.p)
            print ("----------------------------",
                   "Binomial distribution parameters: number of trials = {}; probability = {}".format(self.n, self.p),
                   "----------------------------",
                   sep="\n")
            return self.cls_sampled_distribution
        
        else:
            print ("----------------------------",
                   "ERROR!: {} distribution is not defined within function".format(self.distribution),
                   "----------------------------",
                   sep="\n")
            
     # instance summarise method
    def summarise(self):
        self.summary_min = self.cls_sampled_distribution.min()
        self.summary_max = self.cls_sampled_distribution.max()
        self.summary_mean = self.cls_sampled_distribution.mean()
        self.summary_sd = self.cls_sampled_distribution.std()
        
        print ("----------------------------",
                "Summary stats for {} samples of {} distribution:".format(self.samples, self.distribution),
               "----------------------------",
               "Min = {}".format(self.summary_min),
               "Max = {}".format(self.summary_max),
               "Mean = {}".format(self.summary_mean),
               "Standard Deviation = {}".format(self.summary_sd),
               "END",
               sep="\n")