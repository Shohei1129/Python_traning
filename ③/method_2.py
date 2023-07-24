# 以下の a, b, c の合計が知りたい
a = [1, 2, 3, 4, 5]
b = [1, 10, 100, 1000]
c = [5, 10, 15, 20, 25]

# 与えられた値を合計する関数
def sum(numbers):
    total = 0
    for i in numbers:
        total = total + i   
    return total

d = sum(a)

e = sum(b)

f = sum(c)

print(d, e, f)




# ---以下実行結果 ---
# (15, 1111, 75)