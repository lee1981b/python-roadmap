#!/usr/bin/env python3
"""
This Script Will Search Through A Given File For Email Addresses.
Enter A File In The Input, Include File Path If The File Is Not
In The Current Directory.
"""
import re
# Define the regex pattern for email addresses
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
# Get the file path from the user
file_path = input("Enter File Path: ")
# Open the file and read its content
try:
    with open(file_path, 'r') as file:
        text = file.read()  # Read the content of the file

    # Find all email addresses in the text
    emails = re.findall(pattern, text)

    # Check if any emails were found
    if emails:
        print("Email addresses found:")
        for email in emails:
            print(email)
    else:
        print("No email addresses found.")
except FileNotFoundError:
    print("The specified file was not found.")