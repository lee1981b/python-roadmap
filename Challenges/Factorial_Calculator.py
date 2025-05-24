#!/usr/bin/python3

# Challenge #1: Factorial Calculator

def factorial(n):
    """Return the factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python Factorial_Calculator.py <non-negative-integer>")
        sys.exit(1)
    num = int(sys.argv[1])
    result = factorial(num)
    print(f"Factorial of {num} is {result}")
