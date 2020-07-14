#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Infinite loop, 'a' will always be less than n^3 (except 0 and 1)


b) As n->INF the formula will tail off, so log. Instead of n^2, I say O(n log(n))


c) O(n) : bunnyears always decreasing, 2+ doesn't affect complexity

## Exercise II


<!--
 Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets
 broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less
 than floor f. Devise a strategy to determine the value of f such that the number of
 dropped + broken eggs is minimized. -->

higher floors
 broken
------- (f)
 saved
lower floors

in 2 story building n is 1
in a 20 story building n is 19
f = n-1
O(1)
