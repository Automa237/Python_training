import matplotlib.pyplot as plt
from sklearn import datasets

# digits データをロード
digits = datasets.load_digits()

# 画像を２行５列に表示
for label, img in zip(digits.target[:10], digits.images[:10]):
    plt.subplot(2, 5, label + 1)
    plt.axis("off")
    plt.imshow(img, cmap=plt.cm.gray_r, interpolation="nearest")
    plt.title("Digit: {0}".format(label))
plt.show()

### 分類器を作って評価する

import numpy as np
from sklearn import datasets

# 手書き数字データの読み込み
digits = datasets.load_digits()

# ３と８のデータ位置を決める
flag_3_8 = (digits.target == 2) + (digits.target == 8)

# ３と８のデータを取得
images = digits.images[flag_3_8]
labels = digits.target[flag_3_8]

# 決定木（後述）をインポート
from sklearn import tree

# ３と８の画像データを１次元化
images = images.reshape(images.shape[0], -1)

# 分類器の生成
n_samples = len(flag_3_8[flag_3_8])
train_size = int(n_samples * 3 / 5)
# 決定木というアルゴリズムを使って分類器を生成
classifier = tree.DecisionTreeClassifier()
classifier.fit(images[:train_size], labels[:train_size])

# 分類器を性能（ここでは正答率）を計算する
from sklearn import metrics

expected = labels[train_size:]
predicted = classifier.predict(images[train_size:])
# 正答率の表示
print('Accuracy:\n', 
      metrics.accuracy_score(expected, predicted))
# 混合行列の表示
print('\nConfusion matrix:\n', 
      metrics.confusion_matrix(expected, predicted))
# 適合率の表示
#print('\nPrecision:\n', 
#      metrics.precision_score(expected, predicted, pos_label=3))
# 再現率の表示
#print('\nRecall:\n', 
#      metrics.recall_score(expected, predicted, pos_label=3))
# F値の表示
#print("\nF-measure:\n", 
#      metrics.f1_score(expected, predicted, pos_label=3))