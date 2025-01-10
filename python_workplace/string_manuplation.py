# Original string
text = "  Hello, Python World! Welcome to Python Programming."

# Strip leading and trailing whitespace
stripped_text = text.strip()
print(f"Stripped Text: '{stripped_text}'")  # Removes extra spaces at the start and end

# Convert the string to lowercase
lowercase_text = stripped_text.lower()
print(f"Lowercase Text: '{lowercase_text}'")  # Converts all characters to lowercase

# Replace "Python" with "Rust"
replaced_text = stripped_text.replace("Python", "Rust")
print(f"Replaced Text: '{replaced_text}'")  # Replaces "Python" with "Rust"

# Count occurrences of the word "Python"
count_python = stripped_text.count("Python")
print(f"Count of 'Python': {count_python}")  # Counts how many times "Python" appears

# Check if the string starts with "Hello"
starts_with_hello = stripped_text.startswith("Hello")
print(f"Starts with 'Hello': {starts_with_hello}")  # Checks if it starts with "Hello"

# Check if the string ends with "Programming."
ends_with_programming = stripped_text.endswith("Programming.")
print(f"Ends with 'Programming.': {ends_with_programming}")  # Checks if it ends with "Programming."

# Capitalize the first character of the string
capitalized_text = stripped_text.capitalize()
print(f"Capitalized Text: '{capitalized_text}'")  # Capitalizes only the first character

# Swap the case of each character
swapped_case_text = stripped_text.swapcase()
print(f"Swapped Case Text: '{swapped_case_text}'")  # Swaps uppercase to lowercase and vice versa

print(f" Length = {len(swapped_case_text)}")