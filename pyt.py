#!/usr/bin/python3

if __name__ == "__main__":

    aimlist = ['User', 'Admin', 'others']

    print (f'Welcome to the onboarding portal!.')
    bgn = input('Enter 1 to begin')
    if bgn == 1:
	    name = input('What is your name?')
    	age = input('How old are you?')
    	if age is not int:
	    	age = input('Enter a valid age')
    	origin = input('Where are you from')
    	for A in aimlist:
	    	print(A, end='')
    	aim = input('Select your option aim, 1-3')
        if aim type(int):
    	    if aim < 1 || aim > 3:
    		    print (f'please choose a valid option, 1,2 or 3')
    	    else:
    		    print (f'Welcome {name}! You are here for {aim} services')
        else:
            print f('ERROR!!! enter an option number')
"""
#User
if aim == 1:
    print('You can now have access to centralized information from your community')
    #SHOW POSTS FROM DATABASE [read_posts()] or load posts rendered on feeds.html page
    # <--- ORM ---> IMPLEMENTATION TO BE USED

#Admin
if aim == 2:
    access = input('Enter 1 to login or 2 to sign up')
    if access is not int:
        access = input('Invalid option!\nEnter 1 to login or 2 to sign up')
    elif access == 1:
        username = input('Username')
        password = input('password')
    #    Md_Auth = input('****')

    elif access == 2:
        name = input('What is your name?')
        email = input('email')
        Md_Auth = input('****')
        if Md_Auth == invalid:#"invalid, will be a function that checks for unassigned Md_Auth stored on the database
            print f'WARNING!!!\n [Authorization breach!!!]\n' 
            Md_Auth = input('one more attempt!!')
        password = input('password')
        passchk = input('confirm password')
        if passchk == password:
            print(f'You have successfully become a media {aim}')

        else:
            while passchk !== password:
                password = input('password')
                passchk = input('confirm password')

if aim == 3:
    print('section still in development')
"""
