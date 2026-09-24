string = "Роскомнадзор запретил букву"
[print(string, l) or (string := string.replace(l, '').replace(l.upper(), '')) for l in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" if l in string]