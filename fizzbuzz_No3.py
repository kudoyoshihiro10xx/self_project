xxx = int(input("いくつまで調べますか？: "))

yyy = 0

for yyy in range(1, xxx):
    if yyy % 15 == 0:
        print("FizzBuzz")
    elif yyy % 3 == 0:
        print("Fizz")
    elif yyy % 5 == 0:
        print("Buzz")
    else:
        print(yyy)
