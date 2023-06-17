import random
import string
import re
def generate_password(length, uppercase, digits, special_chars):
    # Составляем строку символов, из которых будет генерироваться пароль
    charset = string.ascii_lowercase
    if uppercase:
        charset += string.ascii_uppercase
    if digits:
        charset += string.digits
    if special_chars:
        charset += string.punctuation

    # Генерируем пароль
    password = ''.join(random.choice(charset) for _ in range(length))

    # Проверяем, удовлетворяет ли пароль заданным требованиям к сложности
    has_uppercase = re.search(r'[A-Z]', password) is not None
    has_digits = re.search(r'\d', password) is not None
    has_special_chars = re.search(r'[^\w\s]', password) is not None

    if uppercase and not has_uppercase:
        password = generate_password(length, uppercase, digits, special_chars)
    elif digits and not has_digits:
        password = generate_password(length, uppercase, digits, special_chars)
    elif special_chars and not has_special_chars:
        password = generate_password(length, uppercase, digits, special_chars)

    return password

if __name__ == '__main__':
    # Задаем требования к паролю
    length = int(input('Введите длину пароля: '))
    uppercase = input('Использовать заглавные буквы (да/нет)? ').lower() == 'да'
    digits = input('Использовать цифры (да/нет)? ').lower() == 'да'
    special_chars = input('Использовать специальные символы (да/нет)? ').lower() == 'да'

    # Генерируем пароль и выводим его на экран
    password = generate_password(length, uppercase, digits, special_chars)
    print(f'Сгенерированный пароль: {password}')
print("goodbye")