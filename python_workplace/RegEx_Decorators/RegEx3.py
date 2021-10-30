
import re

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

# Output: ['Twelve:', ' Eighty nine:', '.']
# If the pattern is not found, re.split() returns a list containing the original string.