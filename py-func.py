# coding: utf-8

def num(x, y):
  ans1 = x + y
  ans2 = x * y
  return ans1

n = num(2, 2)
print n # 4

# repeat文
def repeat(msg, repeat=3):
  for i in range(repeat):
    print msg

repeat("Hello") # Hello, Hello, Hello
repeat("Yey", repeat=5) # Yey, Yey, Yey, Yey, Yey

# グローバル関数
count = 0

def globaltest():
  print count #参照することはできる
  count += 1
  global count  # このグローバル関数を消すとエラーになる
  count += 1
  print count

get_count = globaltest() # 0 , 2

# ラムダ式（lambda)
# ラムダ式は名前のない小さな関数を定義できる。
# ラムダ式自体は式として扱われるため、関数の引数に指定することができる。
my_lambda = lambda x, y: x + y
print my_lambda(5, 5) # 8

a = [1, 2, 3]
print map(lambda x: x ** 2, a)


# 関数を実行する前後に特殊な処理を実行したい場合、＠デコレータを用いることができます。
# 下では、hello関数にmydecolaterの中身を装飾して関数を作れる。
def mydecolater(func):
  def wrapper():
    print "start"
    func()
    print "end"
  return wrapper

@mydecolater
def hello():
  print "hello"

hello() # start, hello, end

# 可変長引数
# 可変長引数の指定、つまり、引数の数を変えることができる
# 何個でも指定できる関数で、「*args」のように変数名の前にアスタリスク(*)を書きます。

def sumArgs(*args):
  v = 0
  for n in args:
    v += n
  return v

print(sumArgs(1,2,3)) # 6
print(sumArgs(1, 2, 3, 4, 5)) # 15

# 辞書型の可変長引数
# 可変長引数を辞書型にマッピングすることができる。
# 「**args」のようにアスタリスク２つを変数名の前に付けます。
def print_args(**args):
  print args

print_args(a=10, b=20, c=40) # ("a": 10, "c": 40, "b": 20)


