import random

def generate_password(length,chars):
        password = ''.join(random.choice(all_chars) for _ in range(length))
        print(password)

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous = 'il1Lo0O'  # неоднозначные символы

# Получаем параметры от пользователя
cntPw = int(input('Укажите количество паролей для генерации: '))
lenPw = int(input('Укажите длину одного пароля: '))
digOn = input('Включать ли цифры 0123456789? (y/n): ').lower() == 'y'
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n): ').lower() == 'y'
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n): ').lower() == 'y'
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n): ').lower() == 'y'
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n): ').lower() == 'y'

# Формируем строку всех возможных символов
all_chars = ''
if digOn:
    all_chars += digits
if ABCon:
    all_chars += uppercase_letters
if abcOn:
    all_chars += lowercase_letters
if chOn:
    all_chars += punctuation

# Исключаем неоднозначные символы, если нужно
if excOn:
    for char in ambiguous:
        all_chars = all_chars.replace(char, '')

# Проверка, что есть хотя бы один символ для генерации
if not all_chars:
    print("Ошибка: не выбрано ни одного набора символов!")
else:
    # Генерируем пароли
    for _ in range(cntPw):
        generate_password(lenPw,all_chars)

