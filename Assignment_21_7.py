"""
Write a recursive python function to print squares of 
first N natural numbers 
"""

def printSquares(n):
    if n > 0:
        printSquares(n - 1)
        print(n ** 2, end=" ")

print()
printSquares(5)
print()
