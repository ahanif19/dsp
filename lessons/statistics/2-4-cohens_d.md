[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

In this exercise, we are asked to determine the *effect size* of whether a child is the first-born in their family (or not). Specifically, we look at its effect on two different metrics, the length of a pregnancy and a child's birth weight.

To do this, we compute Cohen's d using a function provided in the ThinkStats libraries.

```python
CohenEffectSize(firsts.prglngth,others.prglngth)
```

* The pregnancy length for first-born children is approximately <b>0.0288σ</b>  greater than the pregnancy length for children that are not the first born.

```python
CohenEffectSize(firsts['totalwgt_lb'],others['totalwgt_lb'])
```

* First born children's weight is typically <b>0.0887σ</b> lower than the non-first born children's weight.
