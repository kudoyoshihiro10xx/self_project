# 九九の表を作成せよ

# 1 2 3 4 5 6 7 8 9
x = 0
y = 0

for x in range(1, 10):
    for y in range(1, 10):
        print(x * y, end=' ')
    print()
