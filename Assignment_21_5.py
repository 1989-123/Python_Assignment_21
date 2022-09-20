""" 
Write a recursive python function to print first N 
even natural numbers.
"""

def printnEven(n):
    if n > 0:
        printnEven(n - 1)
        print(n * 2, end=" ")

print()
printnEven(10)
print()
