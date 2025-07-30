#!/usr/bin/env python3
# Challenge #2: Fibonacci Calculator

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
