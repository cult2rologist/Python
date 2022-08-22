# !!! JS -> Python WORK №1 !!!
# 1. Создать переменную “item_1”
# 2. Присвоить переменной item_1 цифру 5.
# 3. Вывести в консоль item_1.
item_1 = 5
print(item_1)

# 4. Создать переменную “item_2”
# 5. Присвоить переменной item_2 цифру 3.
# 6. Вывести в консоль item_2.
item_2 = 3
print(item_2)

# 7. Создать переменную “item_3”
# 8. Присвоить переменной item_3 сложение item_1 и item_2.
# 9. Вывести в консоль item_3.
item_3 = item_1 + item_2
print(item_3)

# 10. Создать переменную “item_4”
# 11. Присвоить переменной item_4 строку “Yolochka”
# 12. Вывести в консоль item_4.
item_4 = 'yolochka'
print(item_4)

# 13. Вывести в консоль сложение item_3 и item_4.
result = str(item_3) + item_4
print(result)

# 14. Вывести в консоль умножение item_3 и item_4.
result = item_3 * item_4
print(result)

# 15. Создать переменную “item_5”
# 16. Присвоить переменной item_5 переменную item_3
item_5 = item_3
print(item_5)

# 17. Создать переменную item_6.
# 18. Создать переменную item_6_type
# 19. Присвоить переменной item_6 значение 15
item_6 = 15

# 20. Присвоить переменной item_6_type тип переменной item_6 --- !!! NOT APPLICABLE !!!
# 21. Вывести в консоль тип данных item_6 в виде ——  “item_6 == ”  item_6,  “item_6_type == ”  item_6_type ——
print("item_6 == " + str(type(item_6)))

# 22. Создать переменную item_7 и в ней преобразовать item_6 в String.
item_7 = str(item_6)

# 23. Создать переменную item_7_type
# 24. Присвоить переменной item_7_type тип переменной item_7 --- !!! NOT APPLICABLE !!!
# 25. Вывести в консоль тип данных item_7 в виде ——  “item_7 == ”  item_7,  “item_7_type == ”  item_7_type ——
print("item_7 == " + str(type(item_7)))

# 26. Создать переменную “age_1” и присвоить ей значение 10
# 27. Создать переменную “age_2” и присвоить ей значение 18
# 28. Создать переменную “age_3” и присвоить ей значение 60
# 29. Создать if в котором будете проверять значение переменной age_1
# 30. Если age_1 < age_2, вывести в консоль “You don’t have access cause your age is ” + age_1 + “ It’s less then ”
# 31. Если age_1 >=  age_2 и age_1 <  age_3, вывести в консоль “Welcome  !”
# 32. Если age_1  > age_3, вывести в консоль “Keep calm and watch Culture channel”.
# 33. Иначе выводите “Technical work”.
age_1 = 10
age_2 = 18
age_3 = 60
if age_1 < age_2:
    print("You don't have access cause your age is " +
          str(age_1) + " It's less then " + str(age_2))
elif age_1 >= age_2 | age_1 < age_3:
    print("Welcome!")
elif age_1 > age_3:
    print("Keep calm and watch Culture channel")
else:
    print("Technical work")

# Задания с разным количеством звездочек :)
# 1*:
# Преобразовать написанный код в 26-33 пунктах в функцию, принимающую на вход возраст.
# Вывести в консоль результат работы функции с возрастами 17, 18, 61
def ageFunc(arg_1, arg_2, arg_3):
    if arg_1 < arg_2:
        print("You don't have access cause your age is " +
              str(arg_1) + " It's less then " + str(arg_2))
    elif arg_1 >= age_2 | arg_1 < arg_3:
        print("Welcome!")
    elif arg_1 > arg_3:
        print("Keep calm and watch Culture channel")
    else:
        print("Technical work")

ageFunc(17, 18, 61)

# 2*:
# Преобразовать задание 1* таким образом, чтобы первым делом в функции проверялся тип данных. И если он не Number - кидалась ошибка.
# def ageFunc(arg_1, arg_2, arg_3):
#     numberedArgs = [arg_1, arg_2, arg_3]
#     args = map(int, numberedArgs)
#     if type(list(map(int, args))) != int:
#         print("One of the arguments is not a number")
#     elif arg_1 < arg_2:
#         print("You don't have access cause your age is " +
#               str(arg_1) + " It's less then " + str(arg_2))
#     elif arg_1 >= arg_2 | arg_1 < arg_3:
#         print("Welcome!")
#     elif arg_1 > arg_3:
#         print("Keep calm and watch Culture channel")
#     else:
#         print("Technical work")


# ageFunc(17, 18, 61)

# 3**:
# Преобразовать 2* таким образом, чтобы значение '2' (строка в которой лежит ТОЛЬКО ЦИФРА) пропускалось, преобразовываясь в number
# def ageFunc(arg_1, arg_2, arg_3):
#     numArgs = [arg_1, arg_2, arg_3]
#     intArgs = map(int, numArgs)
#     list(intArgs)
#     if type(intArgs) != int:
#         print("Not a number")
#     elif arg_1 < arg_2:
#         print("You don't have access cause your age is " +
#               str(arg_1) + " It's less then " + str(arg_2))
#     elif arg_1 >= arg_2 | arg_1 < arg_3:
#         print("Welcome!")
#     elif arg_1 > arg_3:
#         print("Keep calm and watch Culture channel")
#     else:
#         print("Technical work")


# ageFunc(17, '18', 61)

# 4***:
# Преобразовать задание 3* таким образом, чтобы возраст вводится используя функцию prompt в привязанной верстке


# !!! JS -> Python WORK №2 !!!
# 1. Написать скриптик, который сосчитает и выведет результат от возведения 2 в степень 10, начиная со степени 1
for power in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(pow(2, power))
# 1*. Преобразовать 1 задачу в функцию, принимающую на вход степень, в которую будет возводиться число 2
def powMe(power):
    print(pow(2, power))

powMe(25)

# 2. Написать скрипт, который выведет 5 строк в консоль таким образом, чтобы в первой строчке выводилось :), во второй :):) и так далее
for i in range(5):
    print(':)')

# 2*. Преобразовать 2 задачу в функцию, принимающую на вход строку, которая и будет выводиться в консоль (как в условии смайлик),
#     а также количество строк для вывода e.g. function printSmile(stroka, numberOfRows)
# def printSmile(strng, numOfRows):

# 3**.  Написать функцию, которая принимает на вход слово. Задача функции посчитать и вывести в консоль, сколько в слове гласных, и сколько согласных букв.
      # e.g. function getWordStructure(word)
      # В консоли:
      # Слово (word) состоит из  (число) гласных и (число) согласных букв

    # Проверки: 'case', 'Case', 'Check-list'

# 4**. Написать функцию, которая проверяет, является ли слово палиндромом
     # e.g. function isPalindrom(word)

    # Проверки: 'abba', 'Abba'
