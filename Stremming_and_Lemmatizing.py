#stremming and Lemmatizing
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

words=["run", "running", "ran", "better", "is"]

stemmer = PorterStemmer()
stemmed_words= [stemmer.stem(word) for word in words]

print("Stemmed Words:")
print(stemmed_words)

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Characters find their true selves
print("Lemmatized Words:")
print(lemmatized_words)
