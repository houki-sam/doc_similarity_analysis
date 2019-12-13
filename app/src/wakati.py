# -*- coding: utf-8 -*-
import os
import sys
from glob import glob

import MeCab
import pickle
import numpy as np
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from sklearn.feature_extraction.text import CountVectorizer

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

    #形態素解析
    tagger = MeCab.Tagger('-Owakati')

    # ファイル名:テキストの辞書を作成    
    corpus_dict = {
        **{path: tagger.parse(docx2doc(path)).strip().split(" ") for path in word_path_list},
        **{path: tagger.parse(pdf2doc(path)).strip().split(" ") for path in pdf_path_list},
    }
    return corpus_dict


def create_models(path):
    #コーパスの辞書を作成
    corpus_dict = create_dict(path)
    
    trainings = [TaggedDocument(words = values, tags = [key]) for key, values in corpus_dict.items()]

    m = Doc2Vec(
        documents= trainings, 
        size=300,
        alpha=0.0025,
        min_alpha=0.000001,
        window=15, 
        min_count=1
        )
    
    # モデルのセーブ
    os.makedirs(stack_dir, exist_ok=True)
    m.save(os.path.join(stack_dir ,"doc2vec.model"))

    array = []
    key_dict = [x for x in corpus_dict.keys()]
    for key in key_dict:
        array.append(m.docvecs[key])
    
    array = np.array(array)
    
    with open(os.path.join(stack_dir,"doc2vec_array.pickle"), mode="wb") as f:
        pickle.dump((key_dict,array), f)

    return m, key_dict, array


    