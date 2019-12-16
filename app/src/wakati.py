# -*- coding: utf-8 -*-
import os
import sys
from glob import glob

import MeCab
import pickle
import numpy as np
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import LabeledSentence
from sklearn.feature_extraction.text import CountVectorizer

from .Text import Text_Data
from settings import stack_dir
from converter.pdf_converter import pdf2doc
from converter.docx_converter import docx2doc


def create_dict(path):
    #比較されるべきファイル
    word_path_list = glob(path + "/*.docx") + glob(path + "/*.doc")
    pdf_path_list = glob(path + "/*.pdf")

    # 対象ファイルがない場合は終了
    if len(word_path_list) + len(pdf_path_list) == 0:
        print("{}にはファイルがありませんでした".format(path))
        sys.exit()

    parser = Text_Data()


    # ファイル名:テキストの辞書を作成    
    corpus_dict = {
        **{path : parser.Text_Data(docx2doc(path)) for path in word_path_list},
        **{path : parser.Text_Data(pdf2doc(path)) for path in pdf_path_list},
    }
    return corpus_dict

def txt2doc(path):
    tagger = MeCab.Tagger('-Owakati')
    with open(path) as f:
        l = f.readlines()
    l = tagger.parse("".join(l)).strip().split(" ")
    return l 


def create_models(path):
    #コーパスの辞書を作成
    txt_path_list = glob("/data/*/*/*/*.txt")

    class LabeledLineSentence(object):
        def __init__(self, filename):
            self.filename = filename
        def __iter__(self):
            for uid, line in enumerate(open(filename)):
                yield LabeledSentence(words=line.split(), labels=['SENT_%s' % uid])
    
    sentences = [LabeledSentence(words = txt2doc(key), tags = [key]) for key in txt_path_list]
    model = Doc2Vec(
        documents = sentences, 
        vector_size = 300,
        alpha = 0.0001,
        min_alpha = .025,
        min_count = 1,
        epoch = 10000,
        dm = 0,
        )
    
    # モデルのセーブ
    os.makedirs(stack_dir, exist_ok=True)
    model.save(os.path.join(stack_dir ,"doc2vec.model"))

    return model




    