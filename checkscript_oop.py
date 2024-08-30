class Innate:
    def __init__(self, name='', age=0, origin=''):
        self.name = name
        self.age = age
        self.origin = origin

    def input_details(self):
        self.name = input('What is your name? ')
        try:
            self.age = int(input('How old are you? '))
        except ValueError:
            print('Enter a valid age next time!')
            exit()
        self.origin = input('Where are you from? ')

    def select_role(self):
        aimlist = ['User', 'Admin', 'Others']
        print("Please select your role:")
        for idx, role in enumerate(aimlist, 1):
            print(f"{idx}. {role}")
        try:
            aim = int(input('Select your option (1-3): '))
            if aim < 1 or aim > 3:
                print('Please choose a valid option, 1, 2, or 3.')
                return None
            return aimlist[aim - 1]
        except ValueError:
            print('ERROR!!! Enter a valid option number.')
            exit()


class User(Innate):
    def __init__(self, name='', age=0, origin=''):
        super().__init__(name, age, origin)

    def access_information(self):
        print('You can now have access to centralized information from your community.')
        # Placeholder for ORM or DB read logic


class Admin(Innate):
    def __init__(self, name='', age=0, origin='', username='', password='', md_auth=''):
        super().__init__(name, age, origin)
        self.username = username
        self.password = password
        self.md_auth = md_auth

    def login(self):
        self.username = input('Username: ')
        self.password = input('Password: ')
        # Placeholder for login logic

    def signup(self):
        self.name = input('What is your name? ')
        self.username = input('Email: ')
        self.md_auth = input('Authorization Code: ')
        invalid = False  # Placeholder for checking invalid auth
        if invalid:
            print('WARNING!!!\n [Authorization breach!!!]\n')
            self.md_auth = input('One more attempt: ')
        self.password = input('Password: ')
        passchk = input('Confirm Password: ')
        while passchk != self.password:
            print('Passwords do not match! Try again.')
            self.password = input('Password: ')
            passchk = input('Confirm Password: ')
        print(f'You have successfully become a media {self.username}')


class Posts:
    def __init__(self, title='', content='', author=''):
        self.title = title
        self.content = content
        self.author = author

    def create_post(self):
        self.title = input('Enter post title: ')
        self.content = input('Enter post content: ')
        self.author = input('Enter author name: ')
        # Placeholder for post creation logic

    def edit_post(self):
        # Placeholder for post editing logic
        pass

    def delete_post(self):
        # Placeholder for post deletion logic
        pass

    def view_posts(self):
        # Placeholder for viewing posts logic
        pass
