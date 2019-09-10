# Single Number

In the solution of this problem, we are going to use [XOR](https://en.wikipedia.org/wiki/Exclusive_or) operator. So, if you do not have any idea about __XOR__ operator, please check out the link.

To solve this problem, we will use following properties of __XOR__ operation:  
```
x^x = 0  
x^0 = x  
Order of operations does not matter, which means XOR of any permutation of n numbers will give the same result  
```
Because of the first and last property, if we __XOR__ our list, elements appear twice will cancel each out. And the remaining one will be our answer  
```
Example:  
nums = [1,3,2,5,3,5,1]  
1^3^2^5^3^5^1 = 1^1^3^3^5^5^2 = 0^2 = 2  
```