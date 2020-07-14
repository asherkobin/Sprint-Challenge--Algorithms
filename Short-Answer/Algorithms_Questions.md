# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:
a = k, b = n^3, f(a) = a + b^2
```python
n = 2

a = 0
2 < 8
a = 4

a = 4
4 < 8
a = 16

a = 16
16 < 16 + 8
a = 24

n = 3

a = 0
3 < 27
a = 9

a = 9
9 < ~800
a = 800

.....



a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
