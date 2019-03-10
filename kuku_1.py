# 九九の表を作成せよ

# 1 2 3 4 5 6 7 8 9
x = 0
y = 0

for x in range(1, 10):
    for y in range(1, 10):
        print('{0:2d} '.format(x * y), end=' ')
    print('')

# print(' | 1 2 3 4 5 6 7 8 9')
# print('--+--------------------------')
# for y in range(1,10):
#   print('{0:2d}|'.format(y),end="")
#   for x in range(1,10):
#     print('{0:2d} '.format(x*y),end="")
#   print('')
