# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
n = 2
a = 0
  while (a < 2 * 2 * 2):
    a = a + 2 * 2

while: 4 < 8
while: 8 < 8

n = 3
a = 0
  while (a < 3 * 3 * 3):
    a = a + 3 * 3

while: 9 < 27
while: 18 < 27
while: 27 < 27

n = 4
a = 0
  while (a < 4 * 4 * 4):
    a = a + 4 * 4

while: 16 < 64
while: 32 < 64
while: 48 < 64
while: 64 < 64





```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
O(n) * O(log(n))
1
2
4
8
16

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
