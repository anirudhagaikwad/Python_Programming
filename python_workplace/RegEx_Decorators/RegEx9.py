# Here, match variable contains a match object.
# Our pattern (\d{3}) (\d{2}) has two subgroups (\d{3}) and (\d{2}). 
# You can get the part of the string of these parenthesized subgroups.


import re

string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string) 

if match:
  print(match.group())
else:
  print("pattern not found")

# Output: 801 35
