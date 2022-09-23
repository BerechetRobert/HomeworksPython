def validation_function():
    while True:
        my_number = input('Introduceti un numar:')
        if my_number == 'exit' or my_number == 'quit':
            break
        try:
            my_number = int(my_number)
            break
        except ValueError:
            print('Introduceti o valoare valida!')
            continue
    return my_number


my_true_number = validation_function()


def palindrome_function():
    if str(my_true_number) == str(my_true_number)[::-1]:
        return True
    else:
        return False


def divisors_function():
    divisors_list = []
    for i in range(1, my_true_number):
        if my_true_number % i == 0:
            divisors_list.append(i)
    return divisors_list


def prime_function():
    if len(divisors_function()) >= 2:
        return False
    else:
        return True


def max_divisor_function():
    for i in range(1, my_true_number)[::-1]:
        if my_true_number % i == 0:
            return i


def digits_function():
    return len(str(my_true_number))
