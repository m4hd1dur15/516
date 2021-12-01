#Project1 --> Chapter1, ex. 24:

from nltk.book import *
print(text6)

#List of all words in text6 that end in -ise:
ending = sorted(w for w in set(text6) if w.endswith('ise')) #The set is used in order to have a single token of a word in a text. I may be used once or n amount of times. A set simply "collapses all duplicates"
print(ending) # sorted is used to generate a sorted list from punctuation, words with capital letters [A-Z], then regular words [a-z].

#List of all words in text6 that contain the letter 'z':
contain = sorted(w for w in set(text6) if "z" in w)
print(contain)

#List of all words in text6 that contain the sequence of letters 'pt':
sequences = sorted(w for w in set(text6) if "pt" in w)
print(sequences)

#List of all words in text6 that contain an initial capital with all lowercase after:
initia = sorted(w for w in set(text6) if w.istitle())
print(initia)

#Chapter1, ex. 25:

sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

#All words beginning with 'sh' in my created list:
start = sorted(w for w in set(sent) if w.startswith('sh'))
print(start)

#All words longer than 4 characters in my created list:
long = sorted(w for w in set(sent) if len(w) > 4)
print(long)
