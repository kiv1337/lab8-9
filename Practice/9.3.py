def duplicates(string):

    b = set()
    numbers = [num for num in string.split()]
    iterator = iter(numbers)

    while True:
        try:
            a = next(iterator)
            if a in b:
                print("YES")
            else:
                print("NO")
                b.add(a)
        except StopIteration:
            break

duplicates("1 2 3 4 1 2 5")
