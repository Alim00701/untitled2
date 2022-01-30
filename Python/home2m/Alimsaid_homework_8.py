import sqlite3


personal_affairs = sqlite3.connect("affairs.sqlite3")
personal = personal_affairs.cursor()

personal.execute(
    """CREATE TABLE IF NOT EXISTS users (
    affairs TEXT, 
    answer TEXT
    )
    """
)
personal_affairs.commit()


def affairs_user():
    global user_affairs
    user_affairs = input('Enter the case and time: ')

    personal.execute(f"SELECT affairs FROM users WHERE affairs = '{user_affairs}'")
    if personal.fetchone() is None:
        personal.execute("INSERT INTO users VALUES (?, ?)", (user_affairs, "no"))
        personal_affairs.commit()
        print('The case is marked')
    for value in personal.execute("SELECT * FROM users"):
        print(value)
    else:
        print('такая заметка уже существует')
        personal_affairs.commit()


# if __name__ == '__main__':
#     affairs_user()
#

def deleter():
    for value in personal.execute("SELECT * FROM users"):
        print(value)
    a = input('Выберите заметку: ')
    personal.execute(f"SELECT affairs FROM users WHERE affairs = '{a}'")
    if personal.fetchone():
        b = input("выполнено или нет?(да или нет)")
        if b == 'да':
            personal.execute(f"DELETE FROM users WHERE affairs = '{a}'")
            print('Заметка удалена')
        elif b == 'нет':
            print('Заметка осталась')
            personal_affairs.commit()


if __name__ == '__main__':
    deleter()
