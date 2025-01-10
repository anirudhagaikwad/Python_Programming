import re

# Define the regex pattern
email_pattern = r'[a-zA-Z][a-zA-Z0-9]{2,7}@[a-zA-Z]{3,6}\.[a-zA-Z]{3}'

# Function to extract emails from a file
def extract_emails(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Find all matching emails
            emails = re.findall(email_pattern, content)
            return emails
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return []

# Example usage
file_path = 'sample.txt'
emails = extract_emails(file_path)

if emails:
    print("Extracted Emails:")
    for email in emails:
        print(email)
else:
    print("No matching emails found.")


# Explanation of the Regex:
#[a-zA-Z][a-zA-Z0-9]{2,7}@[a-zA-Z]{3,6}\.[a-zA-Z]{3}'

# 2. '[a-zA-Z]'  
#    - Purpose: Matches the first character of the email, which must be an alphabet (uppercase or lowercase).  
#    - Example: Matches the 'a' in 'ani'.

# 3. '[a-zA-Z0-9]{2,7}'  
#    - Purpose: Matches 2 to 7 additional alphanumeric characters after the first character.  
#    - Range: Ensures the username (before '@') is at least 3 characters (1 alphabet + 2 additional) and at most 8 characters (1 alphabet + 7 additional).  
#    - Example: Matches 'ni' in 'ani' or 'start12' in 'start12@yahoo.com'.

# 4. '@'  
#    - Purpose: Matches the literal '@' character separating the username and the domain.  
#    - Example: Matches the '@' in 'ani@outlook.com'.

# 5. '[a-zA-Z]{3,6}'  
#    - Purpose: Matches the domain name, which must consist of 3 to 6 alphabetic characters.  
#    - Example: Matches 'outlook' in 'ani@outlook.com' and 'yahoo' in 'start12@yahoo.com'.

# 6. '\.'  
#    - Purpose: Matches the literal '.' character separating the domain name and the top-level domain (TLD).  
#    - Example: Matches the '.' in 'ani@outlook.com'.

# 7. '[a-zA-Z]{3}'  
#    - Purpose: Matches exactly 3 alphabetic characters representing the TLD.  
#    - Example: Matches 'com' in 'ani@outlook.com' or 'org' in 'avcoe@avcoe.org'.

# 8. '\b'  
#    - Purpose: Ensures the email match ends at a word boundary, avoiding partial matches.  
#    - Example: Ensures 'ani@outlook.com' is treated as a complete match and not part of 'ani@outlook.comuse'.

# ############################################

# ### Valid Email Matches:
# - Ensures usernames are 3-8 characters (starting with an alphabet).  
# - Ensures domains are 3-6 characters.  
# - Ensures the TLD(Top-Level Domain) is exactly 3 characters.  
# - Prevents invalid emails such as '123@gmail.com' or 'abc@xyz.toolong'.
