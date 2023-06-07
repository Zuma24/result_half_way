from Python import file_act as file
import Note
import user as u

number = 2  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = u.create_note(number)
    array = file.read()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file.write(array, 'a')
    print('Заметка добавлена...')


def show(text):
    logic = True
    array = file.read()
    if text == 'date':
        date = input('Введите дату в формате дд.мм.гг: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Нет заметок')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = file.read()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = u.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    file.write(array, 'a')
