""" 
Write a recursive python function to print first N natural 
numbers in reverse order
"""

def printNreverse(n):
    if n > 0:
        print(n, end=" ")
        printNreverse(n - 1)

print()
printNreverse(10)
print()
