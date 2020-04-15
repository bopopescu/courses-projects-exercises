def reverse_seq(n):
    seq = list(range(1, n+1,)[::-1])
    print(seq)


print('newline')
reverse_seq(5)

print("\n___________NEW EXERCISE___________\n")

print('Exercise 4-1, page 56')

print("\n")

pizzas = ['margarita', 'pepperoni', 'hawaii', 'cheese']

for pizza in pizzas:
    print(f'I like {pizza} pizza!')
print('In general, I love pizza!')

print("\n")

animals = ['dog', 'cat', 'cow', 'fox', 'wolf']
for animal in animals:
    print(f'{animal.title()} would make a great pet!')
print('Any of these animals would make a great pet!')

print("\n___________NEW EXERCISE___________\n")

for num in range(1, 21):
    print(num)

# million = list(range(1,1000001))
# for num in million:
#    print(num)
# print(sum(million))
# it is as a comment because it's genearte too many lines!
odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

multiples = [value*3 for value in range(3, 31)]
print(multiples)

cubes = [cube**3 for cube in range(1, 10)]
print(cubes)

print("\n___________NEW EXERCISE___________\n")

motorcycles = ['honda', 'yamaha', 'suzuki', 'aprilla', 'ducatti', 'harley davidson', 'royal enfield', 'bmw']
print(motorcycles)
print(f'The first three items in the list are: {motorcycles[0:3]}')
print(f'Three items from the middle of the list are: {motorcycles[3:6]}')
print(f'The las three items in the list are: {motorcycles[-3:]}')

print("\n")

friend_pizzas = pizzas[:]  # original list is on the beginning of this file!
print(pizzas)
print(friend_pizzas)
pizzas.append('new pizza')
friend_pizzas.append('different pizza')
print("\n")

print('My favorite pizzas are:')
print(pizzas)
print('My friends favorite pizzas are:')
print(friend_pizzas)

print("\n___________NEW EXERCISE___________\n")

buffet = ('pizza', 'hamburger', 'fries', 'cheesburger', 'salad')
for meal in buffet:
    print(meal)
print("\n")
buffet = ('sausage', 'hamburger', 'fries', 'cheesburger', 'steak')
print('new buffet menu')
for meal in buffet:
    print(meal.capitalize())

print("\n___________NEW EXERCISE___________\n")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print('hamburger' in buffet)
print('potatoes' in buffet)

print("\n___________NEW EXERCISE___________\n")

alien_color = 'red'
if alien_color == 'green':
    print('Congrats! You just earned 5 points!')
elif alien_color == 'yellow':
    print('Congrats! You just earned 10 points!')
elif alien_color == 'red':
    print('Congrats! You just earned 15 points!')
print('\n')

person_age = 32
if person_age < 2:
    print('This person is a baby!')
elif person_age < 4:
    print('This person is a toddler!')
elif person_age < 13:
    print('This person is a kid!')
elif person_age < 20:
    print('This person is a teenager!')
elif person_age < 65:
    print('This person is an adult!')
elif person_age >= 65:
    print('This person is an elder!')

# the other way to do that!!!
if person_age < 2:
    person_kind = 'baby'
elif person_age < 4:
    person_kind = 'toddler'
elif person_age < 13:
    person_kind = 'kid'
elif person_age < 20:
    person_kind = 'teenager'
elif person_age < 65:
    person_kind = 'adult'
elif person_age >= 65:
    person_kind = 'elder'
# noinspection PyUnboundLocalVariable
print(f'The other way to show that this person is {person_kind}!\n')

favorite_fruit = ['strawberry', 'apple', 'banana']
if 'strawberry' in favorite_fruit:
    print('You really love strawberrys!')
if 'apple' in favorite_fruit:
    print('You really love apples!')
if 'banana' in favorite_fruit:
    print('You really love bananas!')
if 'orange' in favorite_fruit:
    print('You really love oranges!')
if 'berrie' in favorite_fruit:
    print('You really love berries!')

print("\n___________NEW EXERCISE___________\n")

username = []

for name in username:
    if name == 'admin':
        print('Hello Admin! Would you like to see status report?')
    elif name != 'admin':
        print(f'Hello {name.title()}, Thank you for logging again!')
else:
    print('We have to find some users!')

print('\n')

current_users = ['admin', 'adam', 'kacper', 'pawel', 'robert']
new_users = ['stefan', 'radek', 'pawel', 'artur', 'kacper']
uppercases_current_users = current_users[:]

for user in new_users:
    if user in current_users:
        print(f'I am sorry {user.title()} but you have to use a different user name!')
    elif user.upper() in uppercases_current_users:
        print(f'I am sorry {user.title()} but you have to use a different user name!')
    else:
        print(f'{user.title()}, your username is available')

print('\n')

ordinal_numbers = list(range(1, 10))
print(ordinal_numbers)

for num in ordinal_numbers:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')

print("\n___________NEW EXERCISE___________\n")

random_person0 = {'first_name': 'john',
                  'last_name': 'smith',
                  'age': 41,
                  'city': 'london',
                  }
print(random_person0['first_name'].title())
print(random_person0['last_name'].title())
print(random_person0['age'])
print(random_person0['city'].upper())

favorite_number = {'david': 7, 'pamela': 69, 'alice': 100, 'helga': 50, 'alex': 9, }
print(favorite_number['david'])
print(favorite_number['pamela'])
print(favorite_number['alice'])
print(favorite_number['helga'])
print(favorite_number['alex'])

glossary = {
    'python': 'programming language',
    'string': 'abcdefghi...ans so on, etc.',
    'list': '1,2,3,4,5 or car,bike,motocycle',
    'looping': 'going over every things in list,dictionary...etc',
    'dictionary': 'set of keys and values',
    'set': 'printing out unique values from list, dictionaries, etc.',
    'boolean': 'True or False',
    'tuples': 'like a lists but you cant modify',
    'pep8': 'the way to write a clear code',
    'the zen of python': 'philosophy',
    }
print('\npython:')
print(glossary['python'])
print('\nstring:')
print(glossary['string'])
print('\nlist:')
print(glossary['list'])
print('\nlooping:')
print(glossary['looping'])
print('\ndictionary:')
print(glossary['dictionary'])

print("\n___________NEW EXERCISE___________\n")

# shorter and better way to print out info from glossary - loop way!
for word, explanation in glossary.items():
    print(f"\nWord: {word}")
    print(f"Explanation: {explanation}")

print('\n')

rivers = {'nile': 'egypt',
          'vistula': 'poland',
          'tamize': 'england',
          }
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())

favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }
to_poll = ['kuba', 'phil', 'amanda', 'jen', 'mike', 'robert', ]

for name in to_poll:
    if name in favorite_languages:
        print(f"Thank you for your respond {name.title()}!")
    else:
        print(f"{name.title()}, please choose your favorite language")

print("\n___________NEW EXERCISE___________\n")

# random_person0 is little bit upper - from previous exercise!

random_person1 = {'first_name': 'jan',
                  'last_name': 'nowak',
                  'age': 35,
                  'city': 'warszawa',
                  }

random_person2 = {'first_name': 'jesus',
                  'last_name': 'don pedro',
                  'age': 50,
                  'city': 'acapulco',
                  }

people = [random_person0, random_person1, random_person2, ]

for person in people:
    print(person)

print('\n')

pet0 = {'animal': 'dog',
        'owner': 'sarah',
        }

pet1 = {'animal': 'cat',
        'owner': 'paul',
        }

pet2 = {'animal': 'hamster',
        'owner': 'trevor',
        }

pets = [pet0, pet1, pet2, ]

for pet in pets:
    print(pet)

favorite_places = {
    'adam': ['alaska'],
    'sarah': ['china', 'thailand'],
    'albert': ['iceland'],
    'max': ['usa', 'poland', ],
    'tereza': ['mexico', 'italy'],
    }

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name.title()}'s favorite place is:")
        for place in places:
            print(f"\t{place.title()}")
    else:
        print(f"\n{name.title()}'s favorite places are:")
        for place in places:
            print(f"\t{place.title()}")

favorite_number2 = {'david': [7, 81, 123, ],
                    'pamela': [69, 75, ],
                    'alice': [100, 105, ],
                    'helga': [21, 39, 50, 55, ],
                    'alex': [1, 3, 6, 9, 12, ],
                    }

for name, nums in favorite_number2.items():
    print(f"\n{name.title()}'s favorite numbers are: {nums}")

cities = {
    'warsaw': {
        'country': 'poland',
        'population': '2 millions',
        'fact': 'capital of poland',
    },
    'london': {
        'country': 'england',
        'population': '10 millions',
        'fact': 'queen lives there',
    },
    'chicago': {
        'country': 'usa',
        'population': '8 millions',
        'fact': 'windy city',
    },
}

for citie, citie_info in cities.items():
    print(f"\nCitie: {citie.title()}")
    country = f"{citie_info['country']}"
    popul = f"{citie_info['population']}"
    fact = f"{citie_info['fact']}"

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {popul}")
    print(f"\tFact: {fact.capitalize()}")

print("\n___________NEW EXERCISE___________\n")

rental_car = input("Tell us what kind of car would you like to rent?: ")
print(f"Let me see if I can find You a {rental_car}")

dinner_table = input("For how many people you need a table?: ")
dinner_table = int(dinner_table)

if dinner_table > 8:
    print("Sorry you have to wait")
else:
    print('Your table is ready')

multiples_of_ten = input("Please input a number: ")
multiples_of_ten = int(multiples_of_ten)

if multiples_of_ten % 10 == 0:
    print(f"{multiples_of_ten} is multiple of ten!")
else:
    print(f"{multiples_of_ten} is not multiple of ten")

prompt = "\nEnter topping to add on your pizza: "
prompt += "\n(Enter 'quit' when you finished): "

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(f"{toppings.title()} added to your pizza!")
print("Your order is ready")

prompt1 = str("\nWhat is your age?")
prompt1 += "\n(Enter '0' to exit):..."
while True:
    age = int(input(prompt1))
    
    if age == 0:
        break
    elif age < 3:
        print("Your ticket is for free")
        break
    elif age < 12:
        print("Your ticket cost 10$")
        break
    elif age >= 12:
        print("Your ticket cost 15$")
        break
    else:
        print(age)

print('\n')

sandwich_orders = ['tuna', 'pastrami', 'salami', 'pastrami', 'cheese', 'vegge', 'pastrami', 'ham&cheese', ]
finished_sandwiches = []

print("We are out of pastrami sandwiches!\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"Preparing {current_sandwich} sandwich...")
    finished_sandwiches.append(current_sandwich)
    
print("\nThe following sandwiches are ready:")
for sandwich in finished_sandwiches:
    print(sandwich)

responses = {}
polling_active = True

while polling_active:
    name = input("What is your name?: ")
    response = input("If you could visit one place in the world, where would you go? ")
    responses[name] = response
    
    repeat = input("would you like to let another person to respond? (yes/ no): ")
    if repeat == 'no':
        polling_active = False
print("\n--- Pool Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to travel to {response.title()}.")
