# coding: utf-8
#単語をの数をカウントする

#入力された文字列をスペースで分割する
strlist = input().split(" ")
# 重複する文字列を除外する
N = []
for x in strlist:
    if x not in N:
        N.append(x)
# 単語の数をカウントして出力
for i in range(len(N)):
    print(N[i],strlist.count(N[i]))
