# coding: utf-8

# 文字列の処理
# text processing

# 見たい処理のコメント("""で囲った部分)を外してコンパイルする


# リストの場合と,単なる文字列の場合
a = ["str"]
b = "str"
'''
print(a)
'''
# >> ["str"]
'''
print(b)
'''
# >> str

'''
for x in a: print(x)
'''
# >> str
'''
for x in b: print(x)
'''
# >> s
# t
# r

# 文字列を一文字づつ処理する

'''
a = list("str")
b = "str"
print(a)'''
# >> ['s', 't', 'r']
'''
for x in b: print(x)
'''
# >> s
# t
# r
# 文字列を反転してリスト化して一文字づつ返す（リスト化しない場合は別記）
"""
a = "str"
revword = list(reversed(a))
print(revword)
"""
# >> ['r', 't', 's']




# 文字列の整形
# 文字列を左右または中央ぞろえに整形する

# 左揃えにする
# ljust, rjust, centerメソッドは戻り値に左右または両方に指定個のスペースを加えたものを返す
'''
print("|","hej".ljust(20),"|")
'''
# >> | hej                  |
'''
print("|","hej".rjust(20),"|")
'''
# >> |                  hej |
'''
print("|","hej".center(20),"|")
'''
# >> |         hej          |
# スペース以外の文字を追加する場合は引数にその文字を追加する
'''
print("|","hej".center(20,"+"),"|")
'''
# >> | ++++++++hej+++++++++ |


# 文字列両端のスペースを削除する
# lstrip, rstrip, stripメソッドを使う
'''
a = "   hej   "
print("|", a, "|")
print("|", a.lstrip( ), "|")
'''
# >> | hej    |
'''
print("|", a.rstrip( ), "|")
'''
# >> |    hej |
'''
print("|", a.strip( ), "|")
'''
# >> | hej |
# 完全にスペースを取り除く場合は , を + にする
'''
print("|"+ a.strip( )+ "|")
'''
# >> |hej|
# スペース以外の文字列を削除する場合は引数にその文字を指定
'''a = "xyxyxyy hejyx yyx"
print("|"+a.strip("xy")+"|")
'''
# >> | hejyx |


# 文字列の連結
# 複数の小さな文字列を組み合わせて大きな文字列を作る
# 文字列演算子joinを使う
# joinは、文字列のリストに引数をつなげて出力する
'''
str1 = "abc"
str2 = "def"
str3 = "ghi"
strs = [str1,str2,str3]
x =  "".join(strs)
print(x)
'''
# >> abcdefghi
# 特定の文字で区切ってつなげたいときは、引数に文字を指定する
"""
x = ":".join(strs)
print(x)
"""
# >> abc:def:ghi


# 単語を反転させる
"""
a = "str"
revword = a[::-1]
print(revword)
"""
# >> rts


# 文字列中にセットの文字が含まれるか調べる
"""def containsAny(seq, aset):
    """シーケンスseq中にasetのアイテムがひとつでも含まれるかチェックする"""
    for c in seq:
        if c in aset: return True
    return False
a = "りんご"
b = ["X","Y","り"]
print(containsAny(a,b))
"""
# >>> True
# 文字列がセットの文字のみでできているか調べる
"""
def containsOnly(seq, aset):
    #文字列seq中にasetのアイテムのみでできているかチェックする
    for c in seq:
        if c not in aset: return False
    return True
a = "りんご"
b = ["り","ん","ご","の","木"]
print(containsOnly(a,b))
"""
# >> True
"""
a = "りんご"
b = ["りん","ご"]
print(containsOnly(a,b))
"""# asetのアイテムは一文字でなければならない
# >> False


# 文字列の置換
"""
a = "I like orange."
ReplacedStr = a.replace("orange","apple")
print(ReplacedStr)
"""
# >> I like apple.

# 文字列を大文字にしたり小文字にしたりする
string = "abc"
"""
big = string.upper( )
print(big)
"""
# >> ABC
"""
string = "ABC"
small = string.lower( )
print(small)
"""
# >> abc
# 最初の文字だけを大文字に、ほかは小文字にする
"""
a = "one two three"
print(a.title( ))
"""
# >> One two three
# それぞれの単語の最初の文字だけを大文字にする
"""
a = "one two three"
print(a.title( ))
"""
# >> One Two Three

# 文字列の一部にアクセスする
"""
theline = "abcdefghijklmn"
string = theline[3:8]
print(string)
"""
# >> defgh

