#WAP which takes a list of names as arguments and greets 'Hello' to everyone

def greetings(names):
    for name in names:
        print('Hello', name)
        

names = [input('Enter first name: '), 'Sayoni', 'Rounak']
greetings(names)