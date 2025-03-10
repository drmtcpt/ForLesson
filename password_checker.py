def check_password(password):
    has_upr = any(c.isupper() for c in password)  # Исправлено 'chdr' на 'c'
    has_lwr = any(c.islower() for c in password)  # Исправлено 'char' на 'c'
    has_num = any(c.isdigit() for c in password)  # Исправлено 'vhar' на 'c'
    is_long_enough = len(password) >= 8  # Исправлено 'isLongEnough' на 'is_long_enough'
    
    if all([has_upr, has_lwr, has_num, is_long_enough]):
        print('Strong password')
    else:
        print('Weak password')

# Запрос пароля у пользователя и вызов функции проверки
password = input('Enter a password: ')
check_password(password)