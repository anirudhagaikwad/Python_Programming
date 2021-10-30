# Here, we used re.match() function to search pattern within the test_string.
# The method returns a match object if the search is successful.
# If not, it returns None.

import re

pattern='^a...s$'
inp=input("Enter String...: ")
result=re.match(pattern,inp)

if result:
    print("search successful....")
else:
    print("search unsuccessful....")

# Meta Characters = [].^$*+?{}()\|

## [] Squere brackets Meta Characters
# [] --> [abc]   
# [a-e]  [abcde]
# [1-4]  [1234]
# [0-39] [01239]
#[^abc] character except a or b or c 
#[^0-9] its nondigit character

## . Period Meta Characters
# .. acd

## ^ Caret Meta Characters
# ^a
# ^ab
 

## $ Dollar Meta Characters
# a$ 


## * Star Meta Characters
# ma*n  woman   

## + Plus Meta Characters
# ma+n  maaan   woman  man

## ? Question Meta Characters
# ma?n  mn  man  woman

## {} Braces Meta Characters
# a{2,3} abc daat a match daat 
         # aabc  daaat 

## | Alteration Meta Characters 
# a|b acdbea  3 matches 

## () Group Meta Characters        
#(a|b|c)xz --> its matches any string that either a or b or c followed by xz
# axz cabxz 2 matches

## \ Backslash Meta Characters
# \$a
 
 





