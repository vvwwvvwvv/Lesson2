
#функция определяющая переменную №1 и №2. Провереряет, что передано функции строками
def comp_str(str_one,str_two):
    if type(str_one) != str or type(str_two) != str:
        result = 0
    else:
        if str_one == str_two:
            result = 1
        elif len(str_one) > len(str_two):
            result = 2
        elif str_two == 'learn':
            result = 3
        else:
            result = 'Другие случаи'
    return result

#функция выводит на экран результат
def main():
    while True:
        one = input('Первое значение: ')
        two = input('Второе значение: ')

        if one == 'выход':
            break   #прерывает цикл
        else:
            print(comp_str(one,two))


#запускает программу
main()
