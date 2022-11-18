from gensim.models import KeyedVectors
import os

model = KeyedVectors.load_word2vec_format(
os.path.abspath("modelTest.txt"), binary=False)


def findKeyWords(one, two):
    try:
        result = model.most_similar(positive=one, negative=two, topn=2)
        return result
    except:
        return "400"
