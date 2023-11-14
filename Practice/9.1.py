numbers = (2, 4, 8)
proizvedenie = 1
count = 0
iterator = iter(numbers)

try:
    while True:
        num = next(iterator)
        proizvedenie *= num
        count += 1
except StopIteration:
        print("Среднее геометрическое:", (proizvedenie ** (1 / count)))
