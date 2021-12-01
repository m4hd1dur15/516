import re
# import os

getfile = open('inputUK.txt', 'r').read() # This file has a list of UK words from http://www.tysto.com/uk-us-spelling-list.html

USList = re.sub(r"(our)", "or", getfile, flags=re.M) # This looks for the UK "-our" and replaces with US "-or"/ flag is multiline
USList2 = re.sub(r"(mme)", "m", USList, flags=re.M) # This looks for the UK "-mme" and replaces with US "-m"

# print(USList2) # optional

with open('outputUS.txt', 'a+') as writelist: # a+ creates the file for the user in the same directory of the input file without the user needing to do it
    for newlist in USList2:
        writelist.write(newlist)