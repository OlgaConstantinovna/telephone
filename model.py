

def import_dictionary():
    name = input(f'Введите имя:\n ')
    telephone = input(f'Какой номер добавить для "{name}" ?\n')
    data = open('telephone.txt', mode='a',encoding='utf-8')
    data.write(f'{name}: {telephone}\n')
    data.close()


def set_list():
    data = open('telephone.txt', mode='r', encoding='utf-8')
    telephone_list = data.readlines()
    data.close()
    for phrase in telephone_list:
        phrase = phrase.removesuffix('\n')
        phrase = phrase.split(': ')
        print(phrase)


def search_phone():
    data = open('telephone.txt', mode='r', encoding='utf-8')
    telephone_list = data.readlines()
    data.close()
    for phrase in telephone_list:
        phrase = phrase.removesuffix('\n')
        phrase = phrase.split(': ')
        print(phrase)
    name = input('Чей телефон вы хотите найти?: ')
    name = name.lower()
    dictionary = {}
    while True:
        if name in dictionary.keys():
            print(f'{dictionary[phrase]}')
        else:
            print('у вас нет такого контакта')    
        print(name)

        return dictionary
      
            # phrasa = input('Введите ваш запрос: ')

            # # response = telephone_list(query)
            # if phrasa in telephone_list.keys():
            #  print(f'{telephone_list[phrasa]}')
            # else:       
            #  print('Не могу понять вас. Пожалуйста, повторите ваш запрос.')

search_phone()