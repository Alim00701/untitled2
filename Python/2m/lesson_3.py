

class CustomUser:
    def __init__(self, first_name, last_name, email, password, age, gender, phone, secret_key, user_name):
        if isinstance(first_name, str):
            self.first = first_name
        else:
            raise Exception('First name is string')
        if isinstance(last_name, str):
            self.last = last_name
        else:
            raise Exception('Last name is string')
        if isinstance(email, str):
            self.email = email
        else:
            raise Exception('Email is string')
        if isinstance(password, str):
            self.password = password
        else:
            raise Exception('Password is string')
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age is integer')
        if isinstance(gender, str):
            self.gender = gender
        else:
            raise ValueError('Gender is string')
        if isinstance(phone, str):
            self.phone = phone
        else:
            raise ValueError('Phone is integer')
        if isinstance(secret_key, str):
            self.secret = secret_key
        else:
            raise ValueError('Secret key is string')
        if isinstance(user_name, str):
            self.username = user_name
        else:
            raise ValueError('User name is string')

    def __str__(self):
        return f'User name : {self.username}\n' \
               f'First name : {self.first}\n' \
               f'Last name : {self.last}\n' \
               f'Email : {self.email}\n' \
               f'Password : {self.password}\n' \
               f'Age : {self.age}\n' \
               f'Gender : {self.gender}\n' \
               f'Phone : {self.phone}\n' \
               f'Secret Key : {self.secret}\n'

user_1 = CustomUser('Telidas', 'Adilet', 'Saparbek', 'adilet@gmail.com', 23, 'male', '0708167997', 'Bish', 'das')
print(user_1)

class Admin(CustomUser):
    def __init__(self, first_name, last_name, email, password, age, gender, phone, secret_key, user_name):
        super().__init__(first_name, last_name, email, password, age, gender, phone, secret_key, user_name)
    def admin_panel_login(self, password_login):
        if password_login == self.password:
            print('All info')

    def __str__(self):
        return super(Admin, self).__str__()

admin = Admin('Telidas', 'Adilet', 'Saparbek', 'adilet@gmail.com', 23, 'male', '0708167997', 'Bish', 'das')
print(admin)
print(admin.admin_panel_login('123'))

class VIPClient(CustomUser):
    def __init__(self, first_name, last_name, email, password, age, gender, phone, secret_key, user_name):
        super().__init__(first_name, last_name, email, password, age, gender, phone, secret_key, user_name)

    def __str__(self):
        return super(VIPClient, self).__str__()

class SuperUser(Admin, VIPClient):
    def __init__(self, first_name, last_name, email, password, age, gender, phone, secret_key, user_name):
        super().__init__(first_name, last_name, email, password, age, gender, phone, secret_key, user_name)

    def __str__(self):
        return super(SuperUser, self).__str__()

p_user = SuperUser('Telidas', 'Adilet', 'Saparbek', 'adilet@gmail.com', 23, 'male', '0708167997', 'Bish', 'das')
print(p_user)
