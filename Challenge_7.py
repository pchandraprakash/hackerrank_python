"""
Read an integer N.

Without using any string methods, try to print the following:
123...N

Note that "..." represents the values in between.

Important:
print(i, sep=' ', end='', flush=True)

print(i) outputs following result:
1
2
3

print(i, sep=' ', end='', flush=True) outputs following result:
123 (Which is the required output)
"""
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, sep=' ', end='', flush=True)
