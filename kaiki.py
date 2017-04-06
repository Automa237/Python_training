import matplotlib.pyplot as plt
import numpy as np

# 0~1までの乱数を100個作る
x = np.random.rand(100, 1)
x = x * 4 - 2 # 値の範囲を -2 ~ 2 に変更

y = 3 * x - 2 
# 標準正規分布（平均0, 標準偏差 1）の乱数を加える
y += np.random.randn(100, 1)

plt.scatter(x, y, marker="+")
plt.show()

from sklearn import linear_model

model = linear_model.LinearRegression()
model.fit(x, y)

# 得られた直線の関数式 y = ax + b のうち、
# 係数aを出力する
print(model.coef_)
# 切片bを出力する
print(model.intercept_)

r2 = model.score(x, y)
print(r2)