# -*- coding: utf-8 -*-
import os
import sys
from glob import glob

import MeCab
import pickle
import numpy as np
import pandas as pd
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from sklearn.feature_extraction.text import CountVectorizer

from . import wakati
from settings import teaching_dir, test_dir, stack_dir
from converter.pdf_converter import pdf2doc
from converter.docx_converter import docx2doc

def cos(teach_array,test_array):
    bunbo = np.dot(np.linalg.norm(teach_array,axis=1,ord=2)[:,None],np.linalg.norm(test_array,axis=1,ord=2)[None,:])
    bunshi = np.dot(teach_array, test_array.T)
    return bunshi/bunbo

def main(path, learn):
    #検索対象のデータ
    test =wakati.create_dict(path)
    teach = wakati.create_dict(teaching_dir)
    
    
    #分類もとになるデータ
    if learn or not os.path.exists(os.path.join(stack_dir,"doc2vec.model")):
        model = wakati.create_models(teaching_dir)

    else:
        #try:
        model = Doc2Vec.load(os.path.join(stack_dir,"doc2vec.model"))
        
        #except:
            #print("学習データを読み込めませんでした。")
            #sys.exit()
    
    test_key_list = [key for key in test.keys()]
    test_array = []
    for key in test_key_list:
        test_array.append(model.infer_vector(test[key]))

    teach_key_list = [key for key in teach.keys()]
    teach_array = []
    for key in teach_key_list:
        teach_array.append(model.infer_vector(teach[key]))
    
    teach_array = np.array(teach_array)
    test_array = np.array(test_array)

    result = pd.DataFrame(cos(teach_array,test_array),index = teach_key_list, columns=test_key_list)

    result = []
    for x in teach_key_list:
        stack=[]
        for y in test_key_list:
            stack.append(model.docvecs.similarity_unseen_docs(model, teach[x], test[y], alpha=1, min_alpha=0.0001, steps=5))
        result.append(stack)
    
    result = pd.DataFrame(result, index = teach_key_list, columns=test_key_list)    
    result.to_csv("result.csv")



    
    




    



    
    

