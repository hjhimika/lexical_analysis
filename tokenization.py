#Tokenization — Unveiling the Actors

from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

# A scene from our dataset
sentence = "The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away."

# Tokenize into words
word_tokens = word_tokenize(sentence)

# The actors take the stage
print("Word Tokens:")
print(word_tokens)
