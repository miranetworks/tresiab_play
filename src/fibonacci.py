#!/usr/bin/env python

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
        
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b

    return result

#===========================================================

def main(argv=None):
    fib30 = fib(30)
    print fib30

if __name__ == '__main__':
    sys.exit(main())
