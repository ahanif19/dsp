[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

In this exercise, we are asked to plot percentiles of birth weight against mother's age. I started by dividing up mothers' ages into 5-year bins (between 15 and 45). Then I found the 75th, 50th and 25th percentiles of birthweight for each of these bins or groups and plotted them.

Afterward, we were asked to compute and compare the pearson and spearman correlation coefficients for these two variables (birthweight and mother's age).

```python

# Divide mother's age into bins of 5-years, map each observation to its bin and group the data according to the bin it belongs in
bins = np.arange(15,45,5)
idx = np.digitize(live.agepreg,bins)
grps = live.groupby(idx)

ages = [grp.agepreg.mean() for i,grp in grps] # Get the average age in each group
cumdfs = [thinkstats2.Cdf(grp.totalwgt_lb) for i,grp in grps] # Get the CDF of each group

for pct in [75,50,25]:
    bw = [cdf.Percentile(pct) for cdf in cumdfs] # Find the 75th, 50th and 25th percentile birthweight in each age bin
    l = '%dth' % pct
    thinkplot.Plot(ages,bw,label=l) # Plot the birthweight percentiles against average age for each group/bin
    thinkplot.Config(xlabel='Mother\'s Age',ylabel='Birth weight (lbs)',legend=True)
   
# Compute the Pearson Correlation Coefficient
thinkstats2.Corr(live.agepreg,live.totalwgt_lb)

# Compute the Spearman Correlation Coefficient
thinkstats2.SpearmanCorr(live.agepreg,live.totalwgt_lb)
```
Since the Pearson correlation coefficient is slightly less than the Spearman correlation coefficient that might indicate the two variables have a non-linear relationship.
