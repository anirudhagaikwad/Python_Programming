# pass count as a fourth parameter to the re.sub() method
# If omited, it results to 0. 
# This will replace all occurrences.

import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'
replace = ''

new_string = re.sub(r'\s+', replace, string, 1) 
print(new_string)

# Output:
# abc12de 23
# f45 6