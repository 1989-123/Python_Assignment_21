"""
Write a recursive python function to print first N even 
natural numbers in reverse order 
"""

def printnEvenReverse(n):
    if n > 0:
        print(n * 2, end=" ")
        printnEvenReverse(n - 1)

print()
printnEvenReverse(5)
print()
