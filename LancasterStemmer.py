from nltk.stem import LancasterStemmer

# Create a Lancaster Stemmer instance
stemmer = LancasterStemmer()

# Example words to stem
words_to_stem = ['running', 'jumped', 'happily', 'quickly', 'foxes']

# Apply Lancaster Stemmer
stemmed_words = [stemmer.stem(word) for word in words_to_stem]

# Print the results
print("Original words:", words_to_stem)
print("Stemmed words:", stemmed_words)
