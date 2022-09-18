# Functie cu parametrii nedefiniti
def my_function(*args, **kwargs):
    suma = 0
    if type(kwargs) == int:
        suma = kwargs + suma
    for x in args:
        if type(x) == int or type(x) == float :
            suma = x + suma
    return suma

print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4, 'abc', param_1=2))

# Functie recursiva
def my_function(n):
    if n == 0:
        return 0
    return n + my_function(n - 1)

# Suma numerelor de la 0 la n
sum_all = my_function(27)
print('The sum of all numbers from 0 to n is:', sum_all)

# Suma numerelor pare de la 0 la n
def my_even_function(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + my_even_function(n - 2)
    else:
        return my_even_function(n - 1) + my_even_function(n - 3)

even_sum = my_even_function(50)
print('The sum of even numbers from 0 to n is:', even_sum)

# Suma numerelor impare de la 0 la n
def my_odd_function(n):
    if type(n) == int:
        if n <= 0:
            return 0
        if n % 2 == 1:
            return n + my_odd_function(n - 2)
        else:
            return my_odd_function(n - 1)

odd_sum = my_odd_function(20)
print('The sum of odd numbers from 0 to n is:', odd_sum)

# Input function

try:
    a = int(input('a = '))
    print('a =', a)
except (ValueError, NameError) as e:
    if type(e) == NameError:
        print('invalid variable')
    else:
        print('a =', 0)

