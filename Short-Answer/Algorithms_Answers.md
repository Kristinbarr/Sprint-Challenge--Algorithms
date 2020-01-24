#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear Time
As it n grows, it will loop as many time in direct relation to the input n. The variable 'a' is updating similarly to the conditions in the while loop condition. If n is 2, it loops 1 time. If n is 3, it loops 2 times. If n is 4, it loops 3 times, etc.


b) Log-Linear Time
The first for loop iteration count is directly dependant on n. The inner while loop is logarithmic since the conditional logic decreases logarithmically with n. The outer loop still has to run for n times but the inner loop is logarithmic.

c) Constant Time
It is only performing 1 operation. The space complexity is Linear and based on the input.

## Exercise II

Take the middle of the height of floors and drop the egg from there. If the egg breaks, check the middle floor between there and the bottom. If it doesn't break, check the middle floor between there and th top floor. Keep splitting until you find the floor it break on.

The time complexity is O(log(n)) since we are cutting the searching choices in half as we search for the floor that breaks the egg.

