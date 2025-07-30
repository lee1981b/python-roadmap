# Challenge #2: Fibonacci Calculator
Let’s level up with an iterative Fibonacci calculator. 
Fill in the ___ blanks so it prints the n-th Fibonacci number.
Blanks to fill:
    1: Function name
    2: Loop range (how many steps?)
    3: Tuple assignment (a, b = ___, ___)
    4: Entry-point guard ("___")
    5: Argument-count check (what number?)
    6: Recursive call replacement (when printing, call your function)

Script Below:

def ___(n):
    """Return the n-th Fibonacci number."""
    a, b = 0, 1
    for _ in range(___):
        a, b = ___, ___
    return a

if __name__ == "___":
    import sys
    if len(sys.argv) != ___:
        print(f"Usage: python {sys.argv[0]} <non-negative-integer>")
        sys.exit(1)
    num = int(sys.argv[1])
    print(f"Fibonacci({num}) =", ___(num))


Answer: can be found in "Fibonacci_Calculator.py"