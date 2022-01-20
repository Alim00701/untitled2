class Account:
    def __init__(self, name, password, secret_question):
        self.name = name
        self.__password = password
        self._secret = secret_question

    def __password1(self):
        pass

acc = Account('Adilet', '123', secret_question='Bish')
print(acc._password1)
