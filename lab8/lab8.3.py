# for num in (x for x in range(100) if x % 7 == 0):
#     print(num)


def generator():
    n = 7
    while True:
        yield n
        n += 7

result = generator()
for i in result:
    print(i)