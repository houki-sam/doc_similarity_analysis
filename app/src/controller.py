# -*- coding: utf-8 -*-
import os
import sys
from glob import glob

import MeCab
import pickle
import numpy as np
import pandas as pd


from . import wakati
from . import doc2vec
from . import similarity
from converter.pdf_converter import pdf2doc
from converter.docx_converter import docx2doc
from settings import target_dir, stack_dir, model_dir

def main(path, learn):
    target =wakati.create_dict(path)#検索対象のデータ
    
    #try: #学習ずみデータ
    model = doc2vec.return_model(model_dir)
    #except: 
        #print("学習データを読み込めませんでした。")
        #sys.exit()
    
    target_key_list = [key for key in target.keys()]
    target_array = []
    
    result = []
    for x in target_key_list:
        stack=[]
        for y in target_key_list:
            stack.append(
                model.docvecs.similarity_unseen_docs(
                    model, 
                    target[x], 
                    target[y], 
                    alpha = 0.0001,
                    min_alpha = 0.0001,
                    steps = 10,
                    ),
                )
        result.append(stack)
    
    result = pd.DataFrame(result, index = target_key_list, columns=target_key_list)    
    result.to_csv("result.csv")



    
    




    



    
    

