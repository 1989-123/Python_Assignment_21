""" 
Write a recursive python function to print first 
N multiples of a given number.
"""

def printNmultiples(i, n):
    if i != n + 1:
        print(n * i, end=" ")
        i += 1
        printNmultiples(i, n)

print()
printNmultiples(1, 8)
print()
