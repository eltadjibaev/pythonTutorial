def greet(name):
    print(f'Hi there, {name}')

# Parameters
greet('John')

# Keyword Arguments
def greet_user(firstName, lastName):
    print(f'Hi there, {firstName} {lastName}')

greet_user(lastName = 'Smith', firstName = 'John')
