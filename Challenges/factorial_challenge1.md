# Challenge #1: Factorial Calculator
Replace each ___ with the correct Python keyword, operator, or name.
What’s Missing?
    1: The function name (___)
    2: The comparison operator for checking zero (___)
    3: The return statements (___)
    4: The multiplication operator (___)
    5: The recursive call (___)
    6: The entry-point check string (___)

Script Below:

def ___(n):
    """Return the factorial of n."""
    if n ___ 0:
        ___ 1
    else:
        ___ n ___ ___(n-1)

if __name__ == "___":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python Factorial_Calculator.py <non-negative-integer>")
        sys.exit(1)
    num = int(sys.argv[1])
    result = factorial(num)
    print(f"Factorial of {num} is {result}")


Answer: can be found in "Factorial_Calculator.py"
