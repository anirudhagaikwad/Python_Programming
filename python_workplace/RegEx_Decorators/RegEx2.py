# program to extract numbers from string using 're' module
import re

string='hello 12 . hi33 howdy 44'
pattern='\d+'
result=re.findall(pattern,string)
print("Result = ",result)
resultsplit=re.split(pattern,string)
print("Result Split = ",resultsplit)

# r'\n'

## Special Sequence
# \A
# \b
# \B
# \d 
# \D
# \s
# \S
# \w 
# \W 
# \z