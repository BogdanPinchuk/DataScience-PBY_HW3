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
