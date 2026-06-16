from gensim.models import Word2Vec

sentences = [
    ["word2vec", "is", "fun"],
    ["nlp", "is", "powerful"]
]

model = Word2Vec(sentences, vector_size=50, window=3, min_count=1)

print(model.wv.most_similar("word2vec"))