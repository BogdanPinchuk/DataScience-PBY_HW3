from math import sqrt


def print_numbers_by_range(start, stop, step=1, is_row=True):
    """
    Prints numbers between start and stop (inclusive) with step
    :param start: The starting number
    :param stop: The ending number
    :param step: The step size
    :param is_row: Print to line
    """
    if start > stop:
        raise ValueError("Incorrect input data for range!")
    elif step < 1:
        raise ValueError("Incorrect input data for step!")
    else:
        for number in range(start, stop + 1, step):
            if is_row:
                print(number, end=", ") if number < stop else print(number, end="")
            else:
                print(f"- {number}")


def print_entered_numbers():
    """
    Print entered numbers only digits. If the  entered number is "0", then exit from the function.
    """
    info_in_mes = "Enter number: "
    info_out_mes = "Entered number: "
    print('Note. To exit, please enter the "0".\n')
    cmd = input(info_in_mes)
    while cmd != "0":
        if cmd.isdigit():
            print(f"{info_out_mes}{cmd}")
        cmd = input(info_in_mes)
    print('\nProgram finished!')


def find_divisor(number):
    """
    Finds the divisor of a number
    :param number: input number
    :return: message about the divisor or prime number
    """
    if not number.is_integer():
        raise ValueError("Incorrect input integer number!")
    else:
        for value in range(2, number):
            if number % value == 0:
                print(f"Перший дільник числа {number} це {value}.")
                break
        else:
            if number > 1:
                print(f"Число {number} є простим.")


def print_odd_numbers(start, stop):
    """
    Print odd numbers from the range, the stop number included
    :param start: The starting number
    :param stop: The ending number (inclusive)
    """
    if start > stop:
        raise ValueError("Incorrect input data for range!")
    else:
        for number in range(start, stop + 1):
            if number % 2 == 0:  # only for even
                continue
            else:
                print(number, end=", ")
        print("\b\b", end="")


def print_rect_by_sign(num_rows, num_cols, sign='#', left_margin=""):
    """
    Prints a rectangle with given rows and columns by sign
    :param num_rows: The number of rows
    :param num_cols: The number of columns
    :param sign: The sign for printing
    :param left_margin: The left margin for printing
    """
    if num_rows < 1 or num_cols < 1:
        raise ValueError("Incorrect input data!")
    else:
        for row in range(num_rows):
            print(left_margin, end="")
            for col in range(num_cols):
                print(sign, end="")
            print()


def count_positive(numbers):
    """
    Calculate the count of the positive numbers in a list of numbers.
    :param numbers: list of numbers
    :return: count of positive numbers
    """
    if numbers == [] or len(numbers) == 0:
        raise ValueError("Input array is empty!")
    else:
        count = 0
        for number in numbers:
            if number > 0:
                count += 1
        return count


def number_type(n):
    """
    Return the type of number.
    :param n: number
    :return: type of number
    """
    if n < 0:
        return "negative"
    elif n > 0:
        return "positive"
    else:
        return "zero"


def max_in_list(numbers):
    """
    Return the maximum number in a list of numbers.
    :param numbers: list of numbers
    :return: maximum number
    """
    if numbers == [] or len(numbers) == 0:
        return None
    else:
        max_number = numbers[0]
        for index in range(1, len(numbers)):
            if numbers[index] > max_number:
                max_number = numbers[index]
        return max_number


def f(x):
    """
    Calculate the f(x) = sqrt(1/(1+x)) function.
    :param x: input value, requirement: x > -1
    :return: result of f(x)
    """
    try:
        result = sqrt(1.0 / (1 + x))
        return result
    except ZeroDivisionError:
        print(f"Значення \"{x}\" призводить до ділення на нуль!")
    except ValueError:
        print(f"Значення \"{x}\" призводить до комплексного результату!")


def analyze_even_in_num_list(numbers):
    """
    Analyze the evenness of each number in a list.
    :param numbers: list of numbers
    :return: report (number | is even)
    """
    if numbers == [] or len(numbers) == 0:
        raise ValueError("Input array is empty!")
    else:
        is_even = lambda x: x % 2 == 0
        input_list = [is_even(number) for number in numbers]
        dictionary = dict(zip(numbers, input_list))

        srt_col1 = 'Number'
        srt_col2 = ' Is even'
        max_len_lf = len(srt_col1)
        max_len_rt = len(srt_col2)

        for key, value in dictionary.items():
            max_len_lf = max(max_len_lf, len(f"{key}"))
            max_len_rt = max(max_len_rt, len(f"{value}"))

        result = f"{f"{srt_col1}":<{max_len_lf + 1}}|{f"{srt_col2}":^{max_len_rt + 1}}"
        result += f"\n{'-':-^{max_len_lf + max_len_rt + 2}}"
        for key, value in dictionary.items():
            result += f"\n{key:<{max_len_lf + 1}}| {f"{value}":<{max_len_rt + 1}}"
        result += f"\n{'-':-^{max_len_lf + max_len_rt + 2}}"

        output_list = [key for key, value in dictionary.items() if value]
        result += f"\nСписок тільки парних чисел: {output_list}"

        return output_list, result
