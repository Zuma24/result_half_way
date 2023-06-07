import Note


def write(array, mode):
    note1 = open("notes.csv", mode='w', encoding='utf-8')
    note1.seek(0)
    note1.close()
    note1 = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        note1.write(Note.Note.to_string(notes))
        note1.write('\n')
    note1.close


def read():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note.Note(
                id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array
