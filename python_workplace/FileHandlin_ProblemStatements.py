# File Handling in Python
# Writing to a file
print("\nWriting to a file:")
with open("example.txt", "w") as file:
    file.write("Hello, this is an example of file handling in Python.\n")
    file.write(f"Name: {name}, Age: {age}\n")
print("Data has been written to 'example.txt'.")

# Reading from a file
print("\nReading from the file:")
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Appending data to a file
print("\nAppending to the file:")
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")
print("Data has been appended to 'example.txt'.")

# Reading the file again to verify appended data
print("\nReading the updated file:")
with open("example.txt", "r") as file:
    updated_content = file.read()
    print("Updated File Content:\n", updated_content)

# Handling files safely: Check if the file exists before opening
import os

file_path = "example.txt"
if os.path.exists(file_path):
    print("\nDeleting the file for cleanup:")
    os.remove(file_path)  # Delete the file
    print(f"'{file_path}' has been deleted.")
else:
    print(f"File '{file_path}' does not exist.")

# File operations in different modes:
# "r": Read-only mode (default)
# "w": Write mode (overwrites file content)
# "a": Append mode (adds content to the end)
# "x": Create mode (fails if the file exists)
# "r+": Read and write mode
# "w+": Write and read mode

"""
performing arithmetic operations on numbers from a file and saving the results in a new file.
"""
# File names
input_file = "num.txt"
output_file = "results.txt"

# Open the input file to read numbers
with open(input_file, "r") as infile:
    # Read all lines and convert them to a list of integers
    numbers = [int(line.strip()) for line in infile]

# Perform arithmetic operations
results = []  # List to store operation results
for num in numbers:
    # Perform desired operations (example: add, subtract, multiply, divide)
    addition = num + 5
    subtraction = num - 5
    multiplication = num * 2
    division = round(num / 2, 2)  # Rounded to 2 decimal places

    # Append results as a formatted string
    results.append(
        f"Number: {num}, Addition: {addition}, Subtraction: {subtraction}, "
        f"Multiplication: {multiplication}, Division: {division}"
    )

# Write the results to the output file
with open(output_file, "w") as outfile:
    for result in results:
        outfile.write(result + "\n")

print(f"Arithmetic operations completed. Results saved in '{output_file}'.")


### 1. Problem: Count the Frequency of Each Word in a File  
#Write a Python program to read a file, count the frequency of each word, and write the results to another file.


# Read the file and count word frequency
from collections import Counter

try:
    with open("input.txt", "r") as infile:
        # Read all text and split into words
        words = infile.read().split()
        
        # Count word frequencies
        word_count = Counter(words)
        
    with open("word_frequency.txt", "w") as outfile:
        # Write word frequencies to a new file
        for word, count in word_count.items():
            outfile.write(f"{word}: {count}\n")
    print("Word frequencies written to 'word_frequency.txt'")
except FileNotFoundError:
    print("The input file does not exist!")




### 2. Problem: Find and Replace Words in a File  
#Create a program that replaces all occurrences of a specific word in a file with another word and saves the result in the same file.


# Replace a specific word in the file
try:
    with open("example.txt", "r+") as file:
        # Read the file content
        content = file.read()
        
        # Replace occurrences of a word
        content = content.replace("old_word", "new_word")
        
        # Move pointer to the beginning and overwrite the content
        file.seek(0)
        file.write(content)
        file.truncate()  # Remove any leftover content
    print("Word replacement successful.")
except FileNotFoundError:
    print("File not found!")




### 3. Problem: Merge Multiple Files into One  
#Write a program to merge the contents of multiple files into a single file.


# Merge multiple files into one
files_to_merge = ["file1.txt", "file2.txt", "file3.txt"]

try:
    with open("merged.txt", "w") as outfile:
        for file_name in files_to_merge:
            with open(file_name, "r") as infile:
                # Write content of each file to the output file
                outfile.write(infile.read())
                outfile.write("\n")  # Add a newline between files
    print("Files merged into 'merged.txt'.")
except FileNotFoundError as e:
    print(f"Error: {e}")




### 4. Problem: Remove Blank Lines from a File  
#Write a program to remove all blank lines from a file and save the result in the same file.

# Remove blank lines from a file
try:
    with open("file_with_blanks.txt", "r+") as file:
        # Filter out blank lines
        non_blank_lines = [line for line in file if line.strip()]
        
        # Move pointer to the beginning and overwrite the content
        file.seek(0)
        file.writelines(non_blank_lines)
        file.truncate()  # Remove any leftover content
    print("Blank lines removed successfully.")
except FileNotFoundError:
    print("File not found!")


### 5. Problem: Reverse the Content of a File Line by Line  
#Write a program to reverse the content of each line in a file and save it to a new file.


# Reverse the content of each line in a file
try:
    with open("original.txt", "r") as infile:
        # Reverse each line
        reversed_lines = [line.strip()[::-1] + "\n" for line in infile]
    
    with open("reversed.txt", "w") as outfile:
        # Write reversed lines to the new file
        outfile.writelines(reversed_lines)
    print("Content reversed and saved in 'reversed.txt'.")
except FileNotFoundError:
    print("The input file does not exist!")



