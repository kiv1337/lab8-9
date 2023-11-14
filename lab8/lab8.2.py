def geometric_mean(*args):
    if len(args) == 0:
        return 1
    else:
        return args[0] * (geometric_mean(*args[1:])) ** (1 / len(args))


my_tuple = (2, 4, 8)
print(round(geometric_mean(*my_tuple)))
