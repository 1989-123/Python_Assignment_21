"""
Write a recursive python function to print first N odd 
natural numbers in reverse order 
"""

def printnOddReverse(n):
    if n > 0:
        print(n * 2 -1, end=" ")
        printnOddReverse(n - 1)

print()
printnOddReverse(5)
print()
