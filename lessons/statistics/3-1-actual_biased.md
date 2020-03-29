[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

In this exercise, we construct a probability mass function (PMF) for the number of children in a household using two different approaches. The purpose is to demonstrate the <b>class size paradox</b>.

Using the Think Stats functions to construct both a biased and unbiased PMF, we see that the true distribution will differ from the distribution we get by sampling. The reason for this is that the people we sample are inherently more likely to be in larger households than smaller households which skews the distributions and the mean upward.

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
