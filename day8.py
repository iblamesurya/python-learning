# Day 8 - File Handling in Python

import os

# Writing to a file
with open("sample.txt", "w") as f:
    f.write("Hello, Python!\n")
    f.write("Learning file handling today.\n")
    f.write("Day 8 of python learning journey.\n")

# Reading entire file
with open("sample.txt", "r") as f:
    content = f.read()
    print("Full content:")
    print(content)

# Reading line by line
with open("sample.txt", "r") as f:
    print("Line by line:")
    for line in f:
        print(line.strip())

# Appending to a file
with open("sample.txt", "a") as f:
    f.write("Appended this line!\n")

# Reading all lines into a list
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")

# Check if file exists and delete
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("File deleted successfully.")

# Working with file paths
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")
print(f"Files here: {os.listdir('.')}")
