"""
Task
Read an integer N. For all non-negative integers i < N , print i**2. See the sample for details.
"""
if __name__ == '__main__':
    n = int(input())
    r = tuple(range(0,n))
    for i in r:
        print(i**2)