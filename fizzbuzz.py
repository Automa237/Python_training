# coding: utf-8

# fizzbuzz

print("fizzbuzzに関する出力をする")
print("数値nまでのfizzbuzzを出力する場合は1、数値nのfizzbuzzを出力する場合は2を入力")
x = input(" 1 or 2 "+"\n")

if x == str(1):
    n = input("nを入力","\n")
    for x in range(int(n)+1):
        if x % 15 == 0:
            print(x,"fizzbuzz")
        elif x % 3 == 0:
            print(x,"fizz")
        elif x % 5 == 0:
            print(x,"buzz")
        else:
            print(x)
elif x == str(2):
    n = input("nを入力")
    if int(n) % 15 == 0:
        print(n,"fizzbuzz")
    elif int(n) % 5 == 0:
        print(n,"fizz")
    elif int(n) % 3 == 0:
        print(n,"buzz")
    else:
        print(n)
else:
    print("1が2を入力してください")
