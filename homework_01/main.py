"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(number):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
      return  [number ** 2 for number in number]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def prime_numbers(numbers):
    k = 0
    for n in range(1, numbers + 1):
        if numbers % n == 0:
            k += 1
    if k == 2:
        return numbers


def filter_numbers( fnum, numbers ):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if numbers == ODD:
        return [x for x in fnum if x % 2 != 0]
    elif numbers == EVEN:
        return [x for x in fnum if x % 2 == 0]
    elif numbers == PRIME:
        ls_prime = list(filter(prime_numbers, fnum))
        return ls_prime

print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], ODD))
print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], EVEN))
print(filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], PRIME))