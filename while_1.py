


def ask_user():
    ans_dict = {'Как дела?': 'Хорошо', 'Что делаешь?': 'Программирую'}
    while True:
        try:
            ans = input('Пользователь:')
            print(f'Программа: {ans_dict.get(ans, "Я не могу тебе помочь.")}')
        except KeyboardInterrupt:
            print('Пока')
            break


ask_user()
