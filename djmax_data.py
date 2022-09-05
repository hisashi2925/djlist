import pandas as pd
import numpy as np

#soupについて
#1. .textプロパティを用いる(配下のタグはすべて削除される)※重要
#2. str関数で文字列に変換する(自身のタグも出力される)
#3. .contentsにて、配下のタグを全て取得し文字列に変換する(自身のタグは出力されない)



#urlからデータを持ってくる
url = 'https://w.atwiki.jp/djmaxinfo/pages/169.html'

#urlから表(table)にmatch部分があるものを探して持ってくる ※複数検索するものは次元が変わりやすいので注意
dfs = pd.read_html(url, match="アーティスト")

#次元を指定する書き方
#df = pd.DataFrame(dfs[0])

#3次元を2次元に変換する書き方
reshape_dfs = np.reshape(dfs,(504,28))

#dataframeに変換
df = pd.DataFrame(reshape_dfs)

#列を削除
reshape_df=df.drop(columns=df.columns[[0, 6, 7, 25, 26]])

#列名をリストから読み込んで変更
reshape_df.columns = [
    "曲名", 
    "PACK", 
    "カテゴリ", 
    "アーティスト", 
    "BPM", 
    "実装日", 
    "4N", 
    "4H", 
    "4M", 
    "4S", 
    "5N", 
    "5H", 
    "5M", 
    "5S", 
    "6N", 
    "6H", 
    "6M", 
    "6S", 
    "8N", 
    "8H", 
    "8M", 
    "8S", 
    "備考", 
     
]



#csvにして保存
reshape_df.to_csv("D:\python project\django_djmax\djmaxtabledata.csv", index=False, encoding="cp932") #index=Falseで番号削除








