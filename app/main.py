# -*- coding: utf-8 -*-

import sys
from glob import glob
import itertools

import MeCab
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

from src.pdf_converter import pdf2doc
from src.docx_converter import docx2doc


# コサイン類似度の算出式
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


if __name__ == "__main1__":
    # 検索ディレクトリを入力
    path = input("検索するディレクトリ:")
    # ファイルパス合致するものだけ検索
    """
    sone:
        Excelの拡張子なのですが、「xlsx」、「xlsm」、「xls」とあるんで
        この３つのタイプもカバーできますかね？？xlsは古い形式なのでxlrdが
        対応してるといいのですが。。
    """
    docx_path_list = glob(path + "/*.(docx|doc)")
    pdf_path_list = glob(path + "/*.pdf")

    
    if len(docx_path_list) + len(pdf_path_list) == 0:
        print("ファイルがありませんでした")
        sys.exit()

    # ファイル名から文書を抜き出し
    # excel_data = {name: excel2doc(name) for name in excel_path_list}
    # pdf_data = {name: pdf2doc(name) for name in pdf_path_list}
    excel_data = {name: excel2doc(name) if name else '' for name in excel_path_list}
    pdf_data = {name: pdf2doc(name) if name else '' for name in pdf_path_list}

    # 分かち書き

    corpus = []
    col_dict = {}
    i = 0
    for key, item in excel_data.items():
        corpus.append(item)
        col_dict[i] = key
        i += 1

    for key, item in pdf_data.items():
        corpus.append(item)
        col_dict[i] = key
        i += 1

    tagger = MeCab.Tagger('-Owakati')
    corpus = [tagger.parse(sentence).strip() for sentence in corpus]

    vectorizer = CountVectorizer(token_pattern=u'(?u)\\b\\w+\\b')
    bag = vectorizer.fit_transform(corpus)
    bag_of_words = bag.toarray()

    # 重複なし組み合わせでコサイン類似度をだす。
    for col in range(len(col_dict)-1):
        for row in range(1+col, len(col_dict)):
            #類似度
            similar = cos_sim(bag_of_words[col], bag_of_words[row])

            if similar >= 0.7 :
                """
                sone:
                    ここcsvとか出力してくれると最高です！
                    Excelとかでフィルタかければいいので、全分析結果を以下のような感じで出したいですね！
                    col_dict[col], col_dict[row]), similar
                    神田さん含めお手すきのお時間で相談したいです！
                """
                print("{}と{}は類似しています。".format(col_dict[col], col_dict[row]))
