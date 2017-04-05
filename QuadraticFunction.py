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
data_ty = data_x ** 2 #ノイズが乗る前の値。データを正の値にするために、二乗する
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
    
    # 戻り値に学習データ、第二戻り値にトレーニングデータを返す
    return sorted(array[idx_train]), sorted(array[idx_test])

# インデックスリストを分割
indices = np.arange(len(data_x)) # インデックス値のリスト（0~data_x)
# print(indices)
idx_train, idx_test = split_train_test(indices)
# print(idx_train,idx_test)

# 学習データ
x_train = data_x[idx_train] # トレーニングデータとして扱うデータ群をdata_x（もとのデータ）から抽出
y_train = data_vy[idx_train] # トレーニングデータとして扱うデータ群をdata_vy（ノイズ込み）から抽出

# テストデータ
x_test = data_x[idx_test]
y_test = data_vy[idx_test]

## グラフ描画

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