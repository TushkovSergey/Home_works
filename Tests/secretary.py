documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def get_input(text):
    return input(text)

def main():
    while True:
        command = input('Введите команду')
        if command == 'p':
            people()
        elif command == 's':
            shelfs()
        elif command == 'l':
            list1()
        elif command == 'a':
            add()
        elif command == 'd':
            delete_doc()
        elif command == 'm':
            move()
        elif command == 'as':
            add_shelf()
        elif command == 'h':
            print(
                '''Команды:
                p – people – команда, которая запрашивает номер документа и выводит имя человека, которому он принадлежит;
                s – shelf – команда, которая запрашивает номер документа и выводит номер полки, на которой он находится;
                l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
                a – add – команда, которая добавит новый документ в каталог и в перечень полок, запросив его номер, тип, имя владельца и номер полки, на котором он будет храниться;
                d – delete – команда, которая запрашивает номер документа и удаляет его из каталога и из перечня полок.;
                m – move – команда, которая запрашивает номер документа и целевую полку и переместит его с текущей полки на целевую.;
                as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;
                h - help - вывод справки.
                e - exit - выход из программы
                ''')
        elif command == 'e':
            break
        else:
            print("Такой команды нет. Для вывода справки введите h")

def people():
    request_number = get_input("Введите номер документа для выводя имени человека")
    for information in documents:
        number_doc = information.get("number")
        name_doc = information.get("name")
        if number_doc == request_number:
            print(name_doc)

def shelfs():
    request_number = get_input("Введите номер документа для вывода номера полки")
    shelf_number = None
    for shelf in directories:
        number_doc = directories.get(shelf)
        if request_number in number_doc:
            shelf_number = shelf
            print(f'Документ находится на полке {shelf}')
        return f'Документ находится на полке {shelf}'
    if shelf_number == None:
        print("Такого документа нет")

def list1():
    for document in documents:
        type_doc = document.get("type")
        number_doc = document.get("number")
        name_doc = document.get("name")
        print(f'{type_doc} "{number_doc}" "{name_doc}"')

def add(type, number, name, shelf):
    # type = get_input("Введите тип документа")
    # number = get_input("Введите номер документа")
    # name = get_input("Введите имя")
    # shelf = get_input("Введите номер полки")
    if shelf in directories:
        new_string = {"type": type, "number": number, "name": name}
        directories[shelf].append(number)
        documents.append(new_string)
    else:
        print('Такой полки не существует')
    print(documents)
    print(directories)
    return documents

def delete_doc():
    request_number = get_input("Введите номер документа для удаления")
    doc_number = None
    for document in documents:
        number = document.get("number")
        if request_number == number:
            doc_number = number
            documents.remove(document)
    if doc_number == None:
        print("Такого документа нет")
        return 'Такого документа нет'
    else:
        print(f'Документ {doc_number} удален!')

    for shelf in directories:
        doc_number = directories.get(shelf)
        if request_number in doc_number:
            directories[shelf].remove(request_number)
    print(directories)
    return directories[shelf]

def move():
    request_number = input("Введите номер документа для переноса")
    request_shelf = input("Введите номер целевой полки для переноса")
    if request_shelf in directories:
        number = None
        for shelf in directories:
            doc_number = directories.get(shelf)
            if request_number in doc_number:
                number = request_number
                directories[shelf].remove(request_number)
        if number == None:
            print("Такого документа не существует")
        else:
            directories[request_shelf].append(request_number)
    else:
        print("Такой полки нет!")
    print(directories)

def add_shelf():
    request_shelf = input("Введите номер новой полки")
    if request_shelf not in directories:
        directories[request_shelf]=[]
    else:
        print("Такая полка уже есть!")
    print(directories)

if __name__ == '__main__':
    main()

