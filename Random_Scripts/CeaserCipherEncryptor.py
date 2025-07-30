#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This Script Will Emulate The Ancient encryption Algorithm
Known As Ceaser Cipher.
"""

def caesar_cipher():
    secret_message_to_encrypt = input("What Is Your Secret Message You Would Like To Encrypt?: ")
    secret_message_to_encrypt = secret_message_to_encrypt.lower()

    our_secret_message = ""

    shift = int(input("What Is The Shift In Your Cipher?: "))
    direction = input("Would You Like To Shift 'left' or 'right'?: ").strip().lower()

    if direction == 'left':
        shift = -shift  # Negative shift for left

    for char in secret_message_to_encrypt:
        ascii_num = ord(char)

        if 97 <= ascii_num <= 122:  # Process lowercase letters
            new_ascii = ascii_num + shift

            if new_ascii > 122:  # Wrap around if it goes beyond 'z'
                new_ascii = ((new_ascii - 123) % 26) + 97
            elif new_ascii < 97:  # Wrap around if it goes before 'a'
                new_ascii = ((new_ascii - 97) % 26) + 123

            our_secret_message += chr(new_ascii)
        elif 48 <= ascii_num <= 57:  # Process numbers 0-9
            new_ascii = ascii_num + shift

            if new_ascii > 57:  # Wrap around if it goes beyond '9'
                new_ascii = ((new_ascii - 48) % 10) + 48
            elif new_ascii < 48:  # Wrap around if it goes before '0'
                new_ascii = ((new_ascii - 48) % 10) + 58

            our_secret_message += chr(new_ascii)
        else:
            our_secret_message += char  # Non-alphabetic characters remain unchanged

    print("We Have Encrypted Your Secret Message!")
    print(our_secret_message)

if __name__ == "__main__":
    caesar_cipher()