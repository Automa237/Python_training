# coding: utf-8

#素数を探すプログラム
print("nまで素数を判定")
input("nを入力")

for n in range(2,n):
    for x in range(2,n):
        if n % x == 0:
            print(n, "equals", x, "*", n//x)
            break
    else:
        print(n, "is a prime number")
