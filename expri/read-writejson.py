import json

def read_():
    with open("data.json", "r") as f:
        data = json.load(f)
        print(data)

# optionlist = ["read", "write"]
print("enter 1 to write or 2 to read")

option = int(input())

if option == 2:

    x = input("NAME: ")
    y = int(input("AGE: "))
    if y <= 0:
        y=input("Enter a valid age: ")
    elif y > 18:
        print("you are too old :)")
        exit()
    a = input("mother: ")
    b = input("father: ")
    c = input("next of kin: ")
    data = {'name':x, 'age':y, 'mother':a, 'father':b, 'Next of kin':c}
    with open('data.json', 'w') as file:
        json.dump(data, file)
    option = int(input("You have successfully written\n if you wish to READ enter 1or enter 3 to exit"))
    if option == 1:
        read_()
    elif option == 3:
        exit()
elif option == 1:
    read_()
