# Creați un script Python care îndeplinește următoarele funcții:
# Declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine).
print('This is my list:')
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list)

# Afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)
print('Printing my list in ascending order:')
my_ordered_list = sorted(my_list)
print(my_ordered_list[0:]);

# Afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă)
print('Printing my list in descending order:')
print(my_ordered_list[::-1])

# Afișează o listă ce conține numerele pare din lista ordonată (folosind slice)
print('Printing the even numbers in my list:')
print(my_ordered_list[1::2])

# Afișează o listă ce conține numerele impare din lista ordonată (folosind slice)
print('Printing the odd numbers in my list:')
print(my_ordered_list[0::2])

# Afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice).
print('Printing the numbers multiple of 3:')
print(my_ordered_list[2::3])