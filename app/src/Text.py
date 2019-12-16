# coding: utf-8
import sys
import os
import pickle
import numpy as np

import MeCab

class Text_Data(object):
    def __init__(self):
        #形態素解析
        self.tagger = MeCab.Tagger('-Owakati')

    def Text_Data(self, text):
        text = [y for y in sum([x.split('。') for x in text.split('\n')],[]) if len(y)!=0]
        word_list = sum([self.tagger.parse(x).strip().split(" ") for x in text],[])
        

        

        # 除去する文字列を指定
        rems = ['@', ',', '，', '。', ' ', 'http', 'https','//', '、', '×', '.','+', '＋', '/',', ', '(', ')', '（', '）', '://', 'RT', ':', ';','：', '；', '」','「', '＠', '-', '／',  '%', '％', '!', '！', '#', '＃','$', '＄', '=', '＝', 'ー', '￥', '^', '{', '}', '~', '～', '&', '＆', '・', '?', '??', '？', '？？',  '<', '＜', '>', '＞', '_', '＿', 'co', 'jp', '(@', '○', '『', '』', '”', '’', '"', '…',')」', '〇', '【', '】', '[', ']', 'から', 'より', 'こそ', 'でも', 'しか','さえ', 'けれど', 'たり', 'つつ', 'とも','たら', 'ある', 'なら', 'のに', 'です', 'ます', 'する', 'ほど', 'ない', 'くる','なり', 'そう', 'まし', 'その', 'この', 'あの', 'せる', 'どう', 'ため', 'どこ', 'いる', 'これ', 'それ', 'あれ', 'いい', 'など', 'あっ', 'もう', 'さん', 'じゃ','から', 'あり', 'ので', 'とも', 'ませ', 'でし', 'とき', 'こと', 'なる', 'って', 'ただ', 'まで', 'もの', 'つか', 'なっ', 'でき', 'もっ', 'けど', 'ほぼ', 'なー', 'そこ', 'ここ', 'だろ', 'なん', 'だっ', 'なあ', 'っけ', 'せる', 'やっ', 'また','どれ', 'なれ', 'かも', 'いく', 'いけ', 'いう', 'たい', 'あと', 'かも', 'しれ',  'こう', 'なく', 'よく', 'だけ', 'れる', 'よう', 'かけ', 'どの', 'てる', 'とか','という', '思う', '思っ', 'として', 'ところ', 'しまう', 'なんか', 'そんな', 'でしょ', 'しまい', 'わかり', 'まま']

        # 除去リストに数字を追加 
        for number in range(10000):
            rems.append(str(number))

        # 除去リストに追加 ― 一文字のひらがなとカタカナ，全角数字，アルファベット大文字・小文字
        hirakana    = [chr(i) for i in range(12353, 12436)]
        katakana    = [chr(i) for i in range(12449, 12533)]
        zenkaku_num = [chr(i) for i in range(65296, 65296+10)]
        alph_L      = [chr(i) for i in range(97, 97+26)]
        alph_S      = [chr(i) for i in range(65, 65+26)]
        for a in range(len(hirakana)):
            rems.append(hirakana[a])
        for b in range(len(katakana)):
            rems.append(katakana[b])
        for c in range(len(zenkaku_num)):
            rems.append(zenkaku_num[c])
        for d in range(len(alph_L)):
            rems.append(alph_L[d])
        for e in range(len(alph_S)):
            rems.append(alph_S[e])

        rems += hirakana + katakana + zenkaku_num + alph_L + alph_S

        words = [x for x in word_list if x not in rems]

        return words