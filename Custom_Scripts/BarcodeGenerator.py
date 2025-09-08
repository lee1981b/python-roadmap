#!/usr/bin/env python3
"""
This Script Creates Barcodes with random 12 digit integers each time,
also creates a .svg file of the barcode in the current directory.
install dependency's.
pip install python-barcode
"""
import random
from barcode import Code128

def generate_barcode():
    # Generate a random 12-digit number with hyphens
    data = "-".join(["".join(str(random.randint(0, 9)) for _ in range(4)) for _ in range(3)])
    code = Code128(data)
    code.save("barcode")
    print(f"Barcode Generated for: {data}")

# Call the function to generate the barcode
generate_barcode()