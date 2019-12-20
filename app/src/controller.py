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
from settings import target_dir, stack_dir, model_dir, threshold

def main(path, learn):
    target = wakati.create_dict(path)#検索対象のデータ
    
    
    #try: #学習ずみデータ
    model = doc2vec.return_model(model_dir)
    #except: 
        #print("学習データを読み込めませんでした。")
        #sys.exit()
    print(target)
    
    target_key_list = [key for key in target.keys()]
    
        
    result = []
    for x in target_key_list:
        stack=[]
        for y in target_key_list:
            stack.append(
                model.docvecs.similarity_unseen_docs(
                    model, 
                    target[x], 
                    target[y], 
                    ),
                )
        result.append(stack)
    #閾値を超えたものに関して検索をかける
    result_dimension = len(result)
    for x in range(0,result_dimension-1):
        for y in range(x+1,result_dimension):
            if result[x][y] > threshold:
                print("{}と{}は類似度{}で同一文書である可能性が高いです。".format(target_key_list[x],target_key_list[y],result[x][y]))
    
    
    result = pd.DataFrame(result, index = target_key_list, columns=target_key_list)    
    result.to_csv("result.csv")



    
    




    



    
    

