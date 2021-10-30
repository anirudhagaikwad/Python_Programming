# Using r prefix before RegEx

# When r or R prefix is used before a regular expression, it means raw string. 
# For example, '\n' is a new line whereas r'\n' means two characters: a backslash \ followed by n.

# Backlash \ is used to escape various characters including all metacharacters.
#  However, using r prefix makes \ treat as a normal character.

import re

string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string) 
print(result)

# Output: ['\n', '\r']