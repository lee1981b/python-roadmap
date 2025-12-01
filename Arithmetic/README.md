                                             *** Arithmetic ***

# Arithmetic in Python.

**Arithmetic operations** are the basic mathematical operations that form the foundation of many programs.  
Python supports standard operators for addition, subtraction, multiplication, division, and more.

- Common Operators.
```
+ : Addition  
- : Subtraction  
* : Multiplication  
/ : Division (float result)  
// : Floor division (integer result)  
% : Modulus (remainder)  
** : Exponentiation  
```

- Examples.
```python
a = 10
b = 3

print(a + b)   # 13
print(a / b)   # 3.333...
print(a // b)  # 3
print(a ** b)  # 1000
```

- Generating a Multiplication Table.
```
for multiplicant in range(1, 11):
for multiplier in range(1, 4):
    expression = f"{multiplicant:>2d} × {multiplier}"
    product = multiplicant * multiplier
    print(f"{expression} = {product:>2d}", end="\t")
print()
```
