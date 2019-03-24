# 綺麗な九九


vertical_numbers = int(input("縦の列数を入力して下さい:"))
horizontal_numbers = int(input("横の列数を入力して下さい:"))

for vertical_number in range(1, vertical_numbers + 1):
    for horizontal_number in range(1, horizontal_numbers + 1):
        product = vertical_number * horizontal_number
        print('{0} * {1} = {2} |'.format(horizontal_number, vertical_number, product), end='')
    print('')
