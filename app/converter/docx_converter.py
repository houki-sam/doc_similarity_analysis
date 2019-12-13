# -*- coding: utf-8 -*-
import re
import os
import glob
import subprocess

from docx import Document
from docx.shared import RGBColor
from docx.shared import Inches
from docx.shared import Pt

from settings import *

#.docファイルの検索
pattern = re.compile(r'.*.doc$')

def docx2doc(path):
    try:
        #docファイルはファイルの変換を行う
        if pattern.match(path):
            #ファイルの変換
            subprocess.call(['soffice', '--headless', '--convert-to', 'docx', path ,'--outdir', stack_dir ])
            #pathの変更
            filename = path.split("/")[-1].replace(".doc", ".docx")#拡張子をdocxに変更
            path = os.path.join(stack_dir, filename)#pathを変換後ファイルに書き換え
        #ファイルの読み込み
        doc = Document(path)
        #テキスト抽出
        txt = " ".join([par.text for par in doc.paragraphs])
    
    except:
        txt = ""
    
    return re.sub(r"\s|　", '', txt)

