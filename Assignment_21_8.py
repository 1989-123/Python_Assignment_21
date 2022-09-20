"""
Write a recursive python function to print cubes 
of first N natural numbers 
"""

def printCubs(n):
    if n > 0:
        printCubs(n - 1)
        print(n ** 3, end=" ")

print()
printCubs(5)
print()
