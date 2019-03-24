# 九九の表を作成せよ

# 1 2 3 4 5 6 7 8 9
x = 0
y = 0

for x in range(1, 10):
    for y in range(1, 10):
        print('{0:3d}'.format(x * y), end=' ')
    print('')

# 入力した任意の九九表

ccc = int(input("縦の列数を入力して下さい:"))
ddd = int(input("横の列数を入力して下さい:"))

# aaa = 0
# bbb = 0

for aaa in range(1, ccc + 1):
    for bbb in range(1, ddd + 1):
        print('{0:4d}'.format(aaa * bbb), end=' ')
    print('')

# print(' | 1 2 3 4 5 6 7 8 9')
# print('--+--------------------------')
# for y in range(1,10):
#   print('{0:2d}|'.format(y),end="")
#   for x in range(1,10):
#     print('{0:2d} '.format(x*y),end="")
#   print('')


# 綺麗な九九

# eee = int(input("行数を入力して下さい:"))
# fff = int(input("列数を入力して下さい:"))


ccc = int(input("縦の列数を入力して下さい:"))
ddd = int(input("横の列数を入力して下さい:"))

# aaa = 0
# bbb = 0

for aaa in range(1, ccc + 1):
    for bbb in range(1, ddd + 1):
        print('{0:4d}'.format(aaa * bbb), end=' ')
    print('')

    eee = aaa * bbb

    print('{0} * {1} = {2}'.format(ccc, ddd, eee))
