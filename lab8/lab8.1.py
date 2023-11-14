# # #lab6 function
# def numbers(num1, num2):
#     """
#     Эта функция вычисляет произведение двух чисел и затем
#     выводит информацию о том, является ли произведение двузначным числом.
#
#     Args:
#         num1: Первое число.
#         num2: Второе число.
#     """
#     result = num1 * num2
#
#     if 10 <= result and result <= 99 or -99 <= result and result <= -10:
#         print(result,'- двузначное число =)')
#     else:
#         print(result,'- двузначное число =)')
#
# numbers(-2, 20)
#
# # #lab7.1 function
#
# def geometric_mean(numbers):
#     """
#     Вычисляет среднее геометрическое элементов в кортеже.
#
#     Аргументы:
#     numbers (tuple): Кортеж чисел, для которых нужно вычислить среднее геометрическое.
#     """
#     multi = 1
#
#     for el in numbers:
#         multi *= el
#
#     result = multi ** (1 / len(numbers))
#     return round(result)
#
# print('Лабораторная №7.1:', geometric_mean((2, 4, 8)),';')

# lab7.2 function

def odd_numbers(*args):
    """
    Создает список нечетных чисел на основе исходного кортежа.

    Аргументы:
    tuple: Исходный кортеж с целыми числами.
    
    Результат:
    Список, содержащий только нечетные числа из исходного кортежа.
    """
    for x in args:
        if x % 2 != 0:
            print(x)

kortezh = (1, 2, 3, 4, 5, 6, 7, 8, 9)
odd_numbers(*kortezh) #    odd_numbers = [x for x in tuple if x % 2 != 0]

# lab7.3 function

# def check_duplicates(text):
#     """
#     Проверяет, встречались ли числа ранее в строке текста.
#
#     Аргументы:
#     text (str): Строка текста, содержащая числа, разделенные пробелами.
#
#     Результат:
#     Для каждого числа в строке выводит "YES", если число ранее встречалось, и "NO" в противном случае.
#     """
#     numbers_seen = set()
#
#     for num_str in text.split():
#         num = int(num_str)
#         if num in numbers_seen:
#             print("YES")
#         else:
#             print("NO")
#         numbers_seen.add(num)
#
#
# check_duplicates("1 2 3 1 2 3")
