# login system
# ask for a username and password
# or to create an account if they dont have
# theyd fill in email,username, 2 passwords
import json


def write_data(data, filename='data.json'):
    with open(filename, 'w') as doc:
        json.dump(data, doc, indent=1)


def create_acc():
    with open('data.json') as doc:
        data = json.load(doc)
        temp = data['users']
        print('Create Account')
        name = input('username: ')
        email = input('email: ')
        pword = input('password: ')
        while True:
            pword1 = input('confirm password: ')
            if pword == pword1:
                print(
                    f'Hello {name[0:1].upper()+name[1:]}, your account has been successfully created!')
                temp.append({'name': name, 'email': email, 'password': pword})
                write_data(data)
                break
            else:
                print('Invalid input, check your password!')
            continue

# create_acc()


def login():
    print('Login')
    name = input('username: ')
    pword = input('password: ')
    print('logged in successfully!')


# login()
with open('data.json') as doc:
    data = json.load(doc)
    temp = data['users']
    for i in temp:
        if 'noornee' in i['name']:
            print('yh')
            break
        else:
            print('neh')
        break        
