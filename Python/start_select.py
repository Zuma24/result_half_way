import act as a
import user as u


def start():
    input_user = ''
    while input_user != '7':
        u.menu()
        input_user = input().strip()
        if input_user == '1':
            a.show('all')
        if input_user == '2':
            a.add()
        if input_user == '3':
            a.show('all')
            a.id_edit_del_show('del')
        if input_user == '4':
            a.show('all')
            a.id_edit_del_show('edit')
        if input_user == '5':
            a.show('date')
        if input_user == '6':
            a.show('id')
            a.id_edit_del_show('show')
        if input_user == '7':
            u.end()
            break
