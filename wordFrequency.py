#The Symphony of Words: Counter for Word Frequencies.

from collections import Counter

# Our magical dataset
text = "The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away."

# Tokenize the text into words
words = text.lower().split()

# Count word frequencies
word_freq = Counter(words)

# The magical reveal
print("Word Frequencies:")
print(word_freq)
