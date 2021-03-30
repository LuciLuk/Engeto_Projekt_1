USERS = {'user': ['bob', 'ann', 'mike', 'liz'], 'key': ['123', 'pass123', 'password123', 'pass123']}
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
ODDELOVAC = '=' * 70

username = input('Username: ')
password = input('Password: ')
print(ODDELOVAC)

username = username.lower()

if username in USERS['user'] and password == USERS['key'][USERS['user'].index(username)]:
    print(
        f'Welcome to the app, {username[0].upper() + username[1:]}'.center(70),
        'We have 3 texts to be analyzed.'.center(70),
        sep="\n"
    )
    print(ODDELOVAC)
else:
    print('You are not registered user or you used incorrect password.'.center(70))
    quit()

choice = int(input('Enter a number between 1 and 3 to select the text: '))
print(ODDELOVAC)

if choice not in range(1, 4):
    print('You have to fill only numbers between 1 - 3.')
    quit()
else:
