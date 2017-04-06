# coding: utf-8

# 二次関数(y = x*x)のデータを用意して、yの値にノイズを乗せる。
# 実際の実務で扱うデータは、ほとんどがノイズ込みのデータになる。
import numpy as np
import matplotlib.pyplot as plt
# x軸の定義範囲、y軸の定義範囲を指定
x_max = 1
x_min = -1
y_max = 2
y_min = -1
SCALE = 50 # スケール。１単位に何点を使うかを決める
TEST_RATE = 0.3 # トレーニングデータに対するテストデータの割合

# データの生成
data_x = np.arange(x_min, x_max, 1 / float(SCALE)).reshape(-1, 1)
# reshape(a, newshape)関数：配列a全体の要素数はそのままで、shapeをnewshapeに変更する
# 今回は、配列data_xを二次元配列にして、一つ一つの値を配列に格納した
data_ty = data_x ** 2 #ノイズを乗せる前の元のデータ。二次関数( y = x ** 2) を表現している。
data_vy = data_ty + np.random.randn(len(data_ty), 1) * 0.5 # ノイズを乗せる
#plt.plot(data_ty,label="line")
#plt.plot(data_vy,label="line")
#print("もとのデータ＋ノイズが入ったデータ")
#plt.show()

# 学習データとテストデータを分割する（分類問題、回帰問題で使用する）
def split_train_test(array):
    length = len(array) # データの個数
    n_train = int(length * (1 - TEST_RATE)) # 学習データの個数
    
    indices = list(range(length)) # 0からlengthまでの数字が入ったリスト
    np.random.shuffle(indices) # リストを並べ替える
    idx_train = indices[:n_train] # arrayのうち、学習データが入った配列の番号
    idx_test = indices[n_train:] # arrayのうち、学習データが入った配列の番号
    
    # 戻り値に学習データ、第二戻り値にテストデータを返す
    return sorted(array[idx_train]), sorted(array[idx_test])

# インデックスリストを分割
indices = np.arange(len(data_x)) # インデックス値のリスト（0~data_x)
# print(indices)
idx_train, idx_test = split_train_test(indices)
# print(idx_train,idx_test)

# 学習データ
x_train = data_x[idx_train] # 学習データとして扱うデータ群をdata_x（もとのデータ）から抽出
y_train = data_vy[idx_train] # 学習データとして扱うデータ群をdata_vy（ノイズ込み）から抽出

# テストデータ
x_test = data_x[idx_test]
y_test = data_vy[idx_test]

## グラフ描画
"""
# 分析対象点の散布図
# scatterはデータを点で描画する
plt.scatter(data_x, data_vy, label="target")

#　元の線を表示
plt.plot(data_x, data_ty, linestyle=":", label="non noise curve")

# ｘ軸/ｙ軸の範囲を設定
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

# 汎用の表示位置を指定
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)
plt.show()
"""
######
## 分類問題

# 分類ラベル作成

# クラスの閾値（動作が変わるぎりぎりの値）。ここでは原点からの半径
CLASS_RADIUS = 0.6

# 近いか遠いかでクラス分けをする（近いとTrue,遠いとFalse）
labels = (data_x ** 2 + data_vy**2) < CLASS_RADIUS**2

# 学習データ/テストデータに分割
label_train = labels[idx_train] # 学習データ
label_test = labels[idx_test] # テストデータ

"""
### グラフ描画

# 近い/遠いクラス、学習/テストの４種類の散布図を重ねる

plt.scatter(x_train[label_train], y_train[label_train],c="black", s=30, marker="*", label="near train")
plt.scatter(x_train[label_train != True], y_train[label_train != True], c="black", s=30, marker="+", label="far train")

plt.scatter(x_test[label_test], y_test[label_test], c="black", s=30, marker="^", label="near test")
plt.scatter(x_test[label_test != True], y_test[label_test != True], c="black", s=30, marker="x", label="far test")

# 元の線を表示
plt.plot(data_x, data_ty, linestyle=":", label="non noise curve")

# クラスの分離円
circle = plt.Circle((0, 0), CLASS_RADIUS, alpha=0.1, label="near area")  
ax = plt.gca()
ax.add_patch(circle)

# ｘ軸/ｙ軸の範囲を設定
plt.xlim(x_min, x_max) # x軸の範囲設定
plt.ylim(y_min, y_max) # y軸の範囲設定

# 汎用の表示位置を指定
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

# グラフを表示
plt.show()
"""


#### 学習

from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score

data_train = np.c_[x_train, y_train]
data_test = np.c_[x_test, y_test]

# SVMの分類器を作成、学習
classfier = svm.SVC(gamma=1)
classfier.fit(data_train, label_train.reshape(-1))

# Testデータで評価
pred_test = classfier.predict(data_test)
"""
# Accuracyを表示 ※accuracy_score = 正答率
print("accuracy_score:\n", accuracy_score(label_test.reshape(-1), pred_test))

# 混合行列を表示
print("Confusion matrix:\n", confusion_matrix(label_test.reshape(-1), pred_test))
"""

######################
#### 回帰問題

from sklearn import linear_model


### １次式で回帰

# ｘ値
X1_TRAIN = x_train
X1_TEST = x_test

# 学習
model = linear_model.LinearRegression()
model.fit(X1_TRAIN, y_train)

# グラフに描画
plt.plot(x_test, model.predict(X1_TEST), linestyle="-.", label="poly deg 1")

### ２次式で回帰

# ｘ値
X2_TRAIN = np.c_[x_train**2, x_train]
X2_TEST = np.c_[x_test**2, x_test]

# 学習
model = linear_model.LinearRegression()
model.fit(X2_TRAIN, y_train)

# グラフに描画
plt.plot(x_test, model.predict(X2_TEST), linestyle="--", label="poly deg 1")



### ９次式で回帰

# ｘ値
X9_TRAIN = np.c_[x_train**9, x_train**7, x_train**6, x_train**5,
                 x_train**4, x_train**3, x_train**2, x_train] 
X9_TEST = np.c_[x_test**9, x_test**8, x_test**7, x_test**6, x_test**5,
                x_test**4, x_test**3, x_test**2, x_test]

# 学習
model = linear_model.LinearRegression()
model.fit(X9_TRAIN, y_train)

# グラフに描画
#plt.plot(x_test, model.predict(X9_TEST), linestyle="-", label="poly deg 1")


### データの表示

plt.scatter(x_train, y_train, c="black", s=30, marker="v", label="train")
plt.scatter(x_test, y_test, c="black", s=30, marker="x", label="test")

# 元の線を表示
plt.plot(data_x, data_ty, linestyle=":", label="non noise curve")

# ｘ軸/ｙ軸の範囲を設定
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

# 汎用の表示位置を指定
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

# グラフを表示
plt.show()


#########################
#### クラスタリング

from sklearn import cluster

# x, y データを結合
data = np.c_[data_x, data_vy]

# ３つのクラスタに分類
model = cluster.KMeans(n_clusters=3)
model.fit(data)

# dataの分類結果（0~ (n_clusters -1)の番号がつけられている
labels = model.labels_

plt.scatter(data_x[labels == 0], data_vy[labels == 0], c="black", s=30, marker="^", label="cluster 0")
plt.scatter(data_x[labels == 1], data_vy[labels == 1], c="black", s=30, marker="x", label="cluster 1")
plt.scatter(data_x[labels == 2], data_vy[labels == 2], c="black", s=30, marker="*", label="cluster 2")

# 元の線を表示
plt.plot(data_x, data_ty, linestyle=":", label="non noise curve")

# ｘ軸/ｙ軸の範囲を設定
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

# 汎用の表示位置を指定
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

# グラフを表示
plt.show()