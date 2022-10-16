def input_credentials():
    name, surname, birth_date = input("Please enter your name, surname and birth date: \n").split(" ")
    return f"{name}, {surname}, {birth_date}"