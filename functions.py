def greet(name):
    print(f'Hi there, {name}')

# Parameters
greet('John')

# Keyword Arguments
def greet_user(firstName, lastName):
    print(f'Hi there, {firstName} {lastName}')

greet_user(lastName = 'Smith', firstName = 'John')

# Return Statement
def square(number):
    return number * number

result = square(3)
print(result)

# Exceptions
try:
    age = int(input('Age: '))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid value')

