[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```python
# Actual distribution
kid_pmf = thinkstats2.Pmf(resp['numkdhh'],label='actual')

# Biased distribution
kid_biased_pmf = BiasPmf(pmf,label='observed')

# Plot
thinkplot.PrePlot(2)
thinkplot.Pmfs([kid_pmf,kid_biased_pmf])
thinkplot.Config(xlabel='Children',ylabel='PMF')

# Calculate means
kid_pmf.Mean()
kid_biased_pmf.Mean()
```
* We see that the mean is substantially lower for the actual pmf (1.02 children per household), compared to the mean of the reported pmf (2.04 children per household). One of the obvious drivers of the difference is that the actual pmf has many households with zero children. On the other hand, it is is impossible for us to survey a child in a house with no children.
