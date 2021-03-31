USERS = {
    'user': ['bob', 'ann', 'mike', 'liz'],
    'key': ['123', 'pass123', 'password123', 'pass123']
}
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
ODDELOVAC = '=' * 60
counts = {'words': 0, 'titles': 0, 'all_cap': 0,
          'all_low': 0, 'num': 0, 'sum_num': 0}

username = input('Username: ')
password = input('Password: ')
print(ODDELOVAC)

if username.lower() in USERS['user'] \
        and password == USERS['key'][USERS['user'].index(username.lower())]:
    print(
        f'Welcome to the app, {username.title()}'.center(60),
        'We have 3 texts to be analyzed.'.center(60),
        sep="\n"
    )
    print(ODDELOVAC)
else:
    print(
        'Unknown user or incorrect password.'.center(60)
    )
    quit()

choice = input('Enter a number between 1 and 3 to select the text: ')
print(ODDELOVAC)

if choice.isnumeric() and int(choice) in range(1, 4):
    text = TEXTS[int(choice) - 1].split()
    counts['words'] = len(text)
    lenght = {}

    for word in text:
        lenght.setdefault((len(word.strip(',.'))), 0)
        lenght[(len(word.strip(',.')))] += 1
        if word.istitle():
            counts['titles'] += 1
        elif word.isupper():
            counts['all_cap'] += 1
        elif word.islower():
            counts['all_low'] += 1
        elif word.isnumeric():
            counts['num'] += 1
            counts['sum_num'] += int(word)
    print(f'''There are {counts['words']} words in the selected text.''',
    f'''There are {counts['titles']} titlecase words.''',
    f'''There are {counts['all_cap']} uppercase words.''',
    f'''There are {counts['all_low']} lowercase words.''',
    f'''There are {counts['num']} numeric strings.''',
    f'''The sum of all the numbers is {counts['sum_num']}.''',
          sep="\n"
       )
    print(ODDELOVAC)

    print(
        'LEN|'.rjust(5),
        'OCCURENCES'.center(15).ljust(15),
        '|NR.'
    )
    print(ODDELOVAC)
    for index, key in enumerate(sorted(list(lenght.keys()))):
        print(
            f'{index}|'.rjust(5),
            f'{lenght[key] * "*"}'.ljust(15),
            f'|{lenght[key]}'
        )

else:
    print('You have to fill only NUMBERS between 1 - 3.')
