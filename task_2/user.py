class User:
    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} {self.surname}"