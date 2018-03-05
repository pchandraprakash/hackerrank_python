"""
Task
Given an integer, , perform the following conditional actions:

    If is odd, print Weird
    If is even and in the inclusive range of to , print Not Weird
    If is even and in the inclusive range of to , print Weird
    If is even and greater than , print Not Weird
"""
r1 = tuple(range(2,5))
r2 = tuple(range(5,21))

if __name__ == '__main__':
    n = int(input())
if (n % 2 != 0) or (n % 2 == 0 and n in r2):
    print("Weird")
elif (n % 2 == 0 and n in r1) or (n > 20):
    print("Not Weird")
else:
    print("Number out of range")