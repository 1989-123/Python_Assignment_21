"""
Write a recursive python function to 
print a number in reverse order. 
"""

def printReverse(n):
    if n != 0:
        print(n % 10, end="")
        printReverse(n // 10)

print()
printReverse(6784)
print()
