import sqlite3


personal_affairs = sqlite3.connect("affairs")
personal = personal_affairs.cursor()

personal.execute(
    """CREATE TABLE IF NOT EXISTS users (
    affairs TEXT,
    time INT 
    )
    """
)
personal_affairs.commit()


def affairs_user():
    global user_affairs, user_time
    user_affairs = input('Enter the case: ')
    user_time = int(input('Enter the time: '))
    personal.execute(f"INSERT INTO affairs VALUES (?, ?, ?,)", (user_affairs, user_time))
    personal_affairs.commit()
    print('The case is marked')
    for value in personal.execute("SELECT * FROM affairs"):
        print(value)


if __name__ == '__main__':
    affairs_user()

