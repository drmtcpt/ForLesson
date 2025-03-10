def check_password(password):
    has_upr = any(c.isupper() for c in password)  
    has_lwr = any(c.islower() for c in password)  
    has_num = any(c.isdigit() for c in password)  
    is_long_enough = len(password) >= 8      
    if all([has_upr, has_lwr, has_num, is_long_enough]):
        print('Strong password')
    else:
        print('Weak password')

password = input('Enter a password: ')
check_password(password)