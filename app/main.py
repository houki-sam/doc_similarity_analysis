# -*- coding: utf-8 -*-

import sys
from glob import glob

import numpy as np

from src.controller import main
from settings import test_dir


if __name__ == "__main__":
    # 検索ディレクトリを入力
    ExplanatoryText = "検索するディレクトリ(default : {})".format(test_dir)
    path = input(ExplanatoryText)

    # 未入力の場合はデフォルトの場所を検索
    if len(path) == 0:
        path = test_dir

    LearnText = "再学習しますか？Yes or No (default : No)"
    learn = input(LearnText).lower()
    # 未入力の場合は学習をしない
    if learn == "y" or learn == "yes":
        learn = True
    else:
        learn = False


    main(path, learn)
