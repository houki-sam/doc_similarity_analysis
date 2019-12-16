# 文書分類プログラム

## 使い方
1.はじめに以下のURLからファイルをダウンロード
https://www.dropbox.com/s/j75s0eq4eeuyt5n/jawiki.doc2vec.dbow300d.tar.bz2?dl=0
2.コンテナを起動するとファイル"data"ができるのでそこに上記のURLから解凍した.modelファイルを置く。必要があればapp/setting.pyのmodel_dirを書き換える。
3.比較したい対象を"data/teach_data"と"data/test_data"に配置する。
4.docker-compose run にて app/main.py　を実行すると結果がどうディレクトリにresult.csvとして確率で表された形で出てくる。