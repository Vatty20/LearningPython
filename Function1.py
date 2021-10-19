a = range(10)
b = list(range(10))
print(a)
print(b)

b = list(range(5, 10))
print(b) #[5, 6, 7, 8, 9]

b = list(range(5, 11))
print(b) #[5, 6, 7, 8, 9, 10]

x = int(input('Enter first number: ')) #5
y = int(input('Enter second number: ')) #15

b = list(range(x, y, 2)) #increments in steps of 2
print(b) #[5, 7, 9, 11, 13]