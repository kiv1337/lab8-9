first = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
second = []
iterator = iter(first)

try:
    while True:
        num = next(iterator)
        if num % 2 != 0:
            second.append(num)
except StopIteration:
    print(second)
