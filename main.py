# Задание 1

def display_quote():
    quote = (
        "Don't compare yourself with anyone in this world...\n"
        "if you do so, you are insulting yourself.\n"
        "                         — Bill Gates"
    )
    print(quote)

display_quote()

# Задание 2

def display_even_numbers(start, end):
    if start > end:
        start, end = end, start
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    print("Четные числа между {} и {}: {}".format(start, end, even_numbers))
display_even_numbers(10, 20)

# Задание 3

def draw_square(size, symbol, filled):
    if filled:
        for _ in range(size):
            print(symbol * size)
    else:
        if size == 1:
            print(symbol)
        else:
            print(symbol * size)
            for _ in range(size - 2):
                print(symbol + ' ' * (size - 2) + symbol)
            print(symbol * size)

draw_square(5, '*', True)
print()
draw_square(5, '*', False)

# Задание 4

def find_min_of_five(num1, num2, num3, num4, num5):
    """
    Функция возвращает минимальное из пяти чисел.

    :param num1: Первое число
    :param num2: Второе число
    :param num3: Третье число
    :param num4: Четвертое число
    :param num5: Пятое число
    :return: Минимальное число
    """
    return min(num1, num2, num3, num4, num5)

# Задание 5

def product_in_range(lower, upper):
    # Проверяем и меняем местами границы, если нужно
    if lower > upper:
        lower, upper = upper, lower
    product = 1
    for number in range(lower, upper + 1):
        product *= number

    return product
# Пример
print(product_in_range(5, 25))
print(product_in_range(25, 5))
print(product_in_range(1, 4))

min_number = find_min_of_five(5, 3, 8, 1, 4)
print("Минимальное число:", min_number)

# Задание 6

def count_digits(number):
    return len(str(abs(number)))

result = count_digits(3456)
print(f"Количество цифр в числе 3456: {result}")

# Задание 7
def is_palindrome(number):
    num_str = str(number)

    length = len(num_str)

    mid = length // 2

    if length % 2 == 0:
        first_half = num_str[:mid]
        second_half = num_str[mid:][::-1]
    else:
        first_half = num_str[:mid]
        second_half = num_str[mid + 1:][::-1]

    return first_half == second_half


print(is_palindrome(123321))  # True
print(is_palindrome(546645))  # True
print(is_palindrome(421987))  # False


