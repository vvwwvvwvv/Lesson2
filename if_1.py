

#функция определяющая чем должен заниматься пользователь, если его возраст = х
def age_dep(age):
    if age in range(0, 7):
        result = 'Обучается в детском саду'
    elif age in range(8, 17):
        result = 'Обучается в школе'
    elif age in range(18, 24):
        result = 'Обучается в ВУЗ'
    elif age in range(23, 65):
       result = 'Работает'
    elif age in range(66, 120):
        result = 'На пенсии'
    elif age > 120:
        result = 'Потыкай в него палкой, мне кажется, что он мертв'
    else:
        result = 'Возраст не может принимать отрицательное значение'
    return result



def main():
    while True:
        try:
            age = int(input('Введите свой возраст:'))  #просим пользовталея ввести возраст
            res = age_dep(age)
            break       #прерывает цикл
        except ValueError:                  #если возраст отрицательный, результат = некорректный ввод
            res = 'Некоррекетный ввод'
    print(res)


#запускает программу
main()


