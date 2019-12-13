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
    #docファイルはファイルの変換を行う
    if pattern.match(path):
        #ファイルの変換
        print(path)
        subprocess.call(['soffice', '--headless', '--convert-to', 'docx', path ,'--outdir', stack_dir ])
        #pathの変更
        filename = path.split("/")[-1].replace(".doc", ".docx")
        path = os.path.join(stack_dir, filename)
    
    doc = Document(path)
    txt = " ".join([par.text for par in doc.paragraphs])

    return txt

if __name__ == "__main__":
    print(docx2doc("/data/teaching_data/秘密保持契約書 (1).doc"))

