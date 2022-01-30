import sqlite3


database_1 = sqlite3.connect("дом.sqlite3")
sql = database_1.cursor()


sql.execute(
    """CREATE TABLE IF NOT EXISTS users (
    affairs TEXT,
    time TEXT,
    )
    """
)
database_1.commit()


def register_user():
    global user_affairs, user_time
    user_login = input('Login: ')
    user_password = input('Password: ')

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
        database_1.commit()
        print('User registered')
        for value in sql.execute("SELECT * FROM users"):
            print(value)

        else:
            sql.execute(f"DELETE FROM users WHERE login = '{user_login}'")
            database_1.commit()

            for value in sql.execute("SELECT * FROM users"):
                print(value)


if __name__ == "__main__":
    register_user()
