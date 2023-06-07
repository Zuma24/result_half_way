from Python import Note


def create_note(number):
    title = check_text(
        input('Название заметки: '), number)
    body = check_text(
        input('Описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nЭто программа 'Заметки'. Имеются следующие функции:\n"
          "\n1. все заметки"
          "\n2. добавить заметку"
          "\n3. удалить заметку"
          "\n4. редактировать"
          "\n5. выборка заметок по дате"
          "\n6. показать заметку по id"
          "\n7. выход\n"
          "\nВведите номер функции: ")


def check_text(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите текст: ')
    else:
        return text


def end():
    print("До новых встреч!")
