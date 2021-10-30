# pass maxsplit argument to the re.split() method. It's the maximum number of splits that will occur.
# By the way, the default value of maxsplit is 0; meaning all possible splits.

import re

string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'

# maxsplit = 1
# split only at the first occurrence
result = re.split(pattern, string, 1) 
print(result)

# Output: ['Twelve:', ' Eighty nine:89 Nine:9.']
