...
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes
...
n = int(input().strip())

def is_factorial(num):
    i = 1
    factorial = 1
    while factorial < num:
        i += 1
        factorial *= i
    return factorial == num

if is_factorial(n):
    print("Yes")
else:
    print("No")
