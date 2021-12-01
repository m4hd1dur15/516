# Exercise 18:
# Write a program to print the 50 most frequent bigrams (pairs of adjacent words) of a text, omitting bigrams that contain stopwords.
import nltk
import nltk.corpus

from nltk.corpus import stopwords
from nltk.corpus import inaugural
from nltk.probability import FreqDist

gigi = nltk.corpus.stopwords.words('english') # This excludes any stopwords
fifi = nltk.corpus.inaugural.words('2017-Trump.txt') # This is the text I selected to see if any speech pattern appears
fifi2 = (w.lower() for w in fifi if w.isalpha()) # from 6.Summary -Chap.2- It takes care of removing the punctuation

xixi = [w for w in fifi2 if w not in gigi] # This takes care of stripping the text for only bigrams excluding punctuation and stopwords

activity_bigrams = nltk.bigrams(xixi)

make_list = FreqDist(activity_bigrams)
print(make_list.most_common(50))


# Exercise 19:
# Write a program to create a table of word frequencies by genre, like the one given in 1 for modals. Choose your own words and try to find words whose presence (or absence) is typical of a genre. Discuss your findings
# I have used the code from the same chapter and the modal example using Brown corpus.

import nltk
import nltk.corpus
from nltk.corpus import brown
from nltk.inference.tableau import Categories

condi = nltk.ConditionalFreqDist(                     # This was taken from Figure 3.11/ Chap3 (NLTK Book)
            (genre, word)                               
            for genre in brown.categories()
            for word in brown.words(categories=genre))

my_genres = ['news', 'hobbies', 'fiction', 'science_fiction', 'humor']
my_genres2 = ['religion', 'lore', 'belles_lettres', 'romance', 'adventure']
my_words = ['soul', 'emotions', 'heart', 'fit', 'health']
my_words2 = ['soul', 'emotions', 'heart', 'fit', 'health']

print(condi.tabulate(conditions=my_genres, samples=my_words))
print(condi.tabulate(conditions=my_genres2, samples=my_words2))

## The goal is to see different uses of the concept of "heart" in the human body. Either from a spiritual/subjective grading or a physical/objective grading. 
## I applied this differently focusing on "subjective genres" (my_genres2) or more "objective genres" (my_genres).
## Using the visual information provided by the distribution, I intended to make broad obeservations based on the data displayed.

## Observations:
## For my_genre the word "heart" is found across genres and it skews towards with physical/objective side of the use. Very few mentions of the possible subjective aspect of "heart"
## For my_genres2 the word "heart" is found across both sides. 