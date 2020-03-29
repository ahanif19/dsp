[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

In this exercise, we are asked to compute the percentage of the US male population that is eligible to be in the Blue Man Group (i.e. their height is >= 5'10" and <= 6'1"). To do this, I first converted the heights into centimeters, then subtracted the cdf for the minimum height requirement from the cdf of the maximum height requirement.

```python

def convertToCM(height):
    h = height.split('\'')
    feet, inches = float(h[0]), float(h[1])
    cm = (12*feet+inches)*2.54
    return cm

h1 = convertToCM('5\'10')
h2 = convertToCM('6\'1')

dist.cdf(h2)-dist.cdf(h1)
```
The result is that <b>~34% of men</b> are eligible to join Blue Man Group.
