"""
    The main console 
"""
from checkscript_oop import *

if __name__ == "__main__":
    user = Innate

    user.input_details()
    role = user.select_role()

    if role == 'User':
        user  = User(user.name, user.age, user.origin)
        user.access_information()
        print(type(user))
    elif role == 'Admin':
        admin = Admin(user.name, user.age, user.origin)
        print(type(admin))
        access_type = int(input('Enter 1 to Login or 2 to sign up: '))
        if access_type == 1:
            admin.login()
        elif access_type == 2:
            admin.signup()

    elif role =='Others':
        print('This section is still in development.')
else:
    exit()
