#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

n = 1 --> 1
a -> 0 + 1 * 1 = 1

n = 2 --> 8
a -> 0 + 2 * 2 = 4
a -> 4 + 2 * 2 = 8

n = 3 --> 27
a -> 0 + 3 * 3 = 9
a -> 9 + 3 * 3 = 18
a -> 18 + 3 * 3 = 27

n = 4 --> 64
a -> 0 + 4 * 4 = 16
a -> 16 + 4 * 4 = 32
a -> 32 + 4 * 4 = 48
a -> 48 + 4 * 4 = 64

a) O(n) Linear - The number of iterations is dependant on the input directly. Adding up a number to the power of 2 while looping until it's great than the number to the power of 3 will always be one step behind and loop for the value number.


b) O(n log n) Log-linear - The number of iterations will be linear and dependant upon the input and also iterate logarithmically according to input since the conditional for the nested loop is depcreasing logarithmically.


c) O(n) Linear - The number of iterations will be dependant on the input until it reaches the base case.

## Exercise II

O(log(n)) Logarithmic - Going floor by floor will work but the strategy can be improved. The floors are essentially 'in order' since we know that inertia will build up at a predictable rate. We can drop the egg from the middle floor and depending on the outcome, we can identify that the floor it breaks on will be either a higher or lower floor depending on if it breaks. Then we can drop another egg from the middle of that half of the total floors and repeat until the floor is found. 
