"""Coding challenges from chapter two of my Python Book!
Author: Doug Purcell
Website: http://www.purcellconsult.com"""

from functools import reduce
"""coding challenge one."""
def factorial_reduce(n):
    return reduce(lambda x, y : x * y, list(range(1,n+1)))


def factors(n):
    """coding challenge 2. Lists the factors of an integer n"""
    for x in range(1,n+1):
        if n % x == 0:
            print(x)

def fo_shizzle_my_nizzle(n): 
    """coding challenge 3. prints 'fo' or 'shizzle' or 'my' or 'nizzle' depending on the input.""" 
    if n < 0:
        n = "fo"
    elif n >= 1 and n < 50: 
        n = "shizzle"
    elif n >= 50 and n <= 100:
        n = "my"
    elif n % 2 == 0 and n % 3 == 0 and n > 100:
        n = "nizzle"
    else:
        n = ""
    return n


def compute_pattern(n):
    """coding challenge 4. Computes a pattern of numbers."""
    for x in range(1,n):
        for y in range(x, x*2):
            print(y, end= " ")
        print()


def bubble_sort(arr):
    """Coding challenge 5. This is bubble sort, a classic but flawed
    sorting algorithm."""
    temp = None
    for x in range(0, len(arr)-1):
        for y in range(0, len(arr)-1):
            if arr[y] > arr[y+1]:
                temp = arr[y]
                arr[y] = arr[y+1]
                arr[y+1] = temp  
    return arr      


print("coding challenge #1: factorial_reduce(): Inputs: 1, 10, 50")  
fr1 = factorial_reduce(1)
fr2 = factorial_reduce(10)
fr3 = factorial_reduce(50)
print(fr1)
print(fr2)
print(fr3)

print()

print("coding challenge #2: factors(): Inputs: 7,14,20")
factors(7)
print()
factors(14)
print()
factors(20)
print()

print("coding challenge #3: compute_pattern() Inputs: -10...150")
x = -10
"""simple loop that tests input -10...150"""
for x in range(x,151):
    print(x, '=', fo_shizzle_my_nizzle(x))
print()

print("coding challenge #4: compute_pattern() Inputs: 10")
compute_pattern(10)
print()

print("coding challenge #5: bubble_sort(items)")
items = [92, 7, 38, 37, 92, 37, 12, 54, 43, 67, 78, 83, 93, 101, 128, 139, 156]
b = bubble_sort(items)
print(b)






