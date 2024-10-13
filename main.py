string = "Роскомнадзор запретил букву"
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

for letter in alphabet:
    if letter in string:
        print(string, letter)
        string = string.replace(letter, "")
        string = string.replace(letter.upper(), "")
