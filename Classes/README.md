                                             *** Classes ***

# Classes in Python.

A **class** in Python is a blueprint for creating objects (a particular data structure).  
Classes encapsulate data (attributes) and functions (methods) that operate on that data.

### Syntax.
```python
class ClassName:
    def __init__(self, attribute):
        self.attribute = attribute
    
    def method(self):
        return f"Attribute is {self.attribute}"
```

### Example.
```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says woof!"

pet = Dog("Rex")
print(pet.bark())  # Rex says woof!
```

Classes allow for object-oriented programming by combining data and behavior in reusable blueprints.
