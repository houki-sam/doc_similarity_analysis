from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from sklearn.feature_extraction.text import CountVectorizer

def return_model(model_dir):
    return Doc2Vec.load(model_dir)
