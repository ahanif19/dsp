[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)


```python

# Generate the random sample
rand_sample = np.random.random(1000)

# Construct and plot the PMF
width = 0.05
rand_pmf = thinkstats2.Pmf(rand_sample,label='sample')
thinkplot.PrePlot(1)
thinkplot.Hist(rand_pmf, width=width)
thinkplot.Config(xlabel='number',ylabel='PMF')

# Construct and plot the CDF
rand_cdf = thinkstats2.Cdf(rand_sample)
thinkplot.Cdf(rand_cdf)
thinkplot.Config(xlabel='number', ylabel='CDF')
```

* In a uniform distribution, the probability of observing a value between a and b should be 1/(b-a). Since we have 1,000 observations and the likelihood of seeing each value is 0.001, the distribution <b>is uniform</b>.
