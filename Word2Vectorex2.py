
import gensim
from gensim.models import Word2Vec


# Sample sentences for training
sentences = [
    ["I", "love", "natural", "language", "processing"],
    ["Word2Vec", "is", "a", "great", "tool"],
    ["Machine", "learning", "is", "fun"],
    ["Natural", "language", "processing", "is", "awesome"]
]

# CBOW Model
cbow_model = Word2Vec(sentences, vector_size=100, window=2, min_count=1, sg=0)

# Skip-gram Model
skipgram_model = Word2Vec(sentences, vector_size=100, window=2, min_count=1, sg=1)

# Example: Getting the vector for a word
word = "language"
cbow_vector = cbow_model.wv[word]
skipgram_vector = skipgram_model.wv[word]

print(f"CBOW Vector for '{word}':", cbow_vector)
print(f"Skip-gram Vector for '{word}':", skipgram_vector)

# Example: Finding similar words
cbow_similar_words = cbow_model.wv.most_similar(word, topn=5)
skipgram_similar_words = skipgram_model.wv.most_similar(word, topn=5)

print(f"CBOW - Words similar to '{word}':", cbow_similar_words)
print(f"Skip-gram - Words similar to '{word}':", skipgram_similar_words)

