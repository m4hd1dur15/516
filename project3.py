import re
# import os

getfile = open('inputUK.txt', 'r').read() # This file has a list of UK words from http://www.tysto.com/uk-us-spelling-list.html

USList = re.sub(r"(\w{2,})our", r"\1or", getfile, flags=re.M) # This looks for the UK "-our" and replaces with US "-or"/ flag is multiline
USList2 = re.sub(r"(mme)", "m", USList, flags=re.M) # This looks for the UK "-mme" and replaces with US "-m"

# print(USList2) # optional

with open('outputUS.txt', 'a+') as writelist: # a+ creates the file for the user in the same directory of the input file without the user needing to do it
    for newlist in USList2:
        writelist.write(newlist)

# USList = re.sub(r"(\w+)our", r"\1or", getfile, flags=re.M)
# The above doesn't take care of words that do not change like "hour" and "pour"
# The regex would have to also not change if there is a single character before and after the target letters ('our')
# Changed to current variable USList to account for words like "hour" and "pour" that should not change
