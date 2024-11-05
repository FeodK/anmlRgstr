class Animal:
    def __init__(self, name, birth_date, command=None):
        self.__name = name
        self.__birth_date = birth_date
        self.__command = command if command else []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_birth_date(self):
        return self.__birth_date

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date

    def get_commands(self):
        return self.__command

    def add_command(self, command):
        self.__command.append(command)

class DomesticAnimal(Animal):
    def __init__(self, name, birth_date, command=None):
        super().__init__(name, birth_date, command)

class PackAnimal(Animal):
    def __init__(self, name, birth_date, command=None):
        super().__init__(name, birth_date, command)
