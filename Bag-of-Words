# Bag-of-Words — Crafting the Script

from sklearn.feature_extraction.text import CountVectorizer

# Characters speak in our story
documents = ["I love coding.", "Coding is fun."]

# Craft the script – Bag-of-Words
vectorizer = CountVectorizer(stop_words=None,token_pattern=r'\b\w+\b')
#token_pattern=r'\b\w+\b counts single character
bow_matrix = vectorizer.fit_transform(documents)

# The script unfolds
print("Bag-of-Words Representation:")
print(bow_matrix.toarray())

print("Vocabulary:")
print(vectorizer.get_feature_names_out())
