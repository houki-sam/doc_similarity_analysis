# -*- coding: utf-8 -*-
import sys
from glob import glob

from .pdf_converter import docx2doc
from .docx_converter import pdf2doc


def controll(path):

    #比較されるべきファイル
    word_path_list = glob(path + "/*.(docx|doc)")
    pdf_path_list = glob(path + "/*.pdf")


    if len(word_path_list) + len(pdf_path_list) == 0:
        print("ファイルがありませんでした")
        sys.exit()
    
    excel_data = {name: excel2doc(name) if name else '' for name in word_path_list}
    pdf_data = {name: pdf2doc(name) if name else '' for name in pdf_path_list}

controll("/data")