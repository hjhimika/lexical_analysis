from nltk.stem import PorterStemmer

# The characters' diverse forms
words = ["run", "running", "ran"]

# The magical transformation – Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]

# The characters' true essence
print("Stemmed Words:")
print(stemmed_words)
