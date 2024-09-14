#!/usr/bin/python3
"""Non-OOP approach to the news software service"""

if __name__ == "__main__":
    # Initialize list of possible user roles
    aimlist = ['User', 'Admin', 'Others']

    # Welcome message
    print(f'Welcome to the onboarding portal!')

    # Begin the process
    try:
        bgn = int(input('Enter 1 to begin: '))  # Convert input to integer
    except ValueError:
        print('Invalid input! Please enter a valid number.')
        exit()

    if bgn == 1:
        # Gather user information
        name = input('What is your name? ')
        age = input('How old are you? ')
        try:
            age = int(age)  # Convert age to integer
        except ValueError:
            print('Enter a valid age next time!')
            exit()

        origin = input('Where are you from? ')
        
        # Display role options
        print("Please select your role:")
        for idx, role in enumerate(aimlist, 1):
            print(f"{idx}. {role}")
        
        # Select user role
        try:
            aim = int(input('Select your option (1-3): '))
        except ValueError:
            print('ERROR!!! Enter a valid option number.')
            exit()

        if aim < 1 or aim > 3:
            print('Please choose a valid option, 1, 2, or 3.')
        else:
            print(f'Welcome {name}! You are here for {aimlist[aim - 1]} services.')

        # User actions
        if aim == 1:
            print('You can now have access to centralized information from your community.')
            # Placeholder: Implement ORM or DB read logic here

        # Admin actions
        elif aim == 2:
            try:
                access = int(input('Enter 1 to login or 2 to sign up: '))
            except ValueError:
                print('Invalid option! Please enter 1 or 2.')
                exit()

            if access == 1:
                username = input('Username: ')
                password = input('Password: ')
                # Placeholder: Implement login logic here

            elif access == 2:
                name = input('What is your name? ')
                email = input('Email: ')
                Md_Auth = input('Authorization Code: ')
                
                # Placeholder: Function to check for invalid authorization code
                invalid = False  # Example flag, change based on actual logic
                if invalid:
                    print('WARNING!!!\n [Authorization breach!!!]\n')
                    Md_Auth = input('One more attempt: ')
                
                password = input('Password: ')
                passchk = input('Confirm Password: ')
                
                while passchk != password:
                    print('Passwords do not match! Try again.')
                    password = input('Password: ')
                    passchk = input('Confirm Password: ')
                
                print(f'You have successfully become a media {aimlist[aim - 1]}')

        # Other roles or options
        elif aim == 3:
            print('This section is still in development.')

    else:
        print('Process terminated.')

