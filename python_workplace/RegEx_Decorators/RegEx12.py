# Suppose you want to find the email address inside the string 'xyz alice-b@google.com purple monkey'.
# We'll use this as a running example to demonstrate more regular expression features. 
# Here's an attempt using the pattern r'\w+@\w+'


import re

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
  print(match.group())  ## 'b@google'
