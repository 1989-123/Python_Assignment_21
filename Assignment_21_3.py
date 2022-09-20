""" 
Write a recursive python function to print 
first N odd natural numbers
"""

def printnOdd(n):
    if n > 0:
        printnOdd(n - 1)
        print(n * 2 - 1, end=" ")

print()
printnOdd(5)
print()
