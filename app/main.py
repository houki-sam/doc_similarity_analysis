# -*- coding: utf-8 -*-

import sys
from glob import glob

import numpy as np

from src.controller import main
from settings import target_dir


if __name__ == "__main__":

    # 検索ディレクトリを入力
    path = input("検索するディレクトリ(default : {})".format(target_dir))
    # 未入力の場合はデフォルトの場所を検索
    if len(path) == 0:
        path = target_dir
    
    args = sys.argv
    #あとで再学習についてのプログラムを書く
    main(path, False)
