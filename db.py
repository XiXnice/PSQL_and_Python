from work_db import DB

database = str(input('Введите название БД: '))
user = str(input('Введите имя пользователя: '))
password = str(input('Введите пароль: '))
command = 0

if __name__ == '__main__':
    db = DB(database, user, password)
    db.create_db()

while command != 8:
    command = int(input('(1)Добавить клиента\n(2)Добавить телефон для существующего клиента\n(3)Изменить данные о клиенте\n(4)Изменить номер телефона клиента\n(5)Удалить телефон для существующего клиента\n(6)Удалить существующего клиента\n(7)Найти клиента по его данным\n(8)Exit\nВведите номер команды: '))
    if command == 1:
        db.new_client()
    elif command == 2:
        db.inf_client()
    elif command == 3:
        db.change_data()
    elif command == 4:
        db.change_number()
    elif command == 5:
        db.delete_phone()
    elif command == 6:
        db.delete_client()
    elif command == 7:
        db.find_сlient()
    elif command == 8:
        print('Exit')
    elif command <1 or command > 7:
        print('Ошибка команды')
    else:
        print('Ошибка')
