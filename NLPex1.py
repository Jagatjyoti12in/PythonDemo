import gensim
from gensim.models import Word2Vec

# Sample sentences for training
sentences = [
    ["I", "love", "natural", "language", "processing"],
    ["Word2Vec", "is", "a", "great", "tool"],
    ["Machine", "learning", "is", "fun"],
]

# Train the Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=1)

# Get the vector for a word
vector = model.wv['language']
print("Vector for 'language':", vector)

# Find similar words
similar_words = model.wv.most_similar('language', topn=5)
print("Words similar to 'language':", similar_words)
