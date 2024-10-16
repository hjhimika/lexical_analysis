# Sentence Tokenization:
from nltk.tokenize import sent_tokenize

# Our dataset unfolds with multiple scenes
text = "The quick brown fox jumps over the lazy dog. The dog barks, and the fox runs away."

# Tokenize into sentences
sentence_tokens = sent_tokenize(text)

# Scenes become acts
print("Sentence Tokens:")
print(sentence_tokens)
