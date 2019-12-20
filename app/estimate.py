import os
import sys
import glob

from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

from src.text import Text_Data

if __name__ == "__main__":
    dirs = glob.glob("/data/livedoor/text/*/*.txt")
    lists = []
    SplitClass = Text_Data()
    for path in dirs:
        with open(path, mode="r") as f:
            lines = f.readlines()
        lists.append(SplitClass(lines[0]))
    trainings = [TaggedDocument(words = data,tags = [i]) for i,data in enumerate(lines)]

    m = Doc2Vec(
        documents= trainings,
        min_alpha = 0.0001,
        min_count=5,
        window=15,
        epoch=15,
        vector_size=300,
        )

    m.save("/data/livedoor/doc2vec.model")
    