#append
#insert
#sort
#pop
#clear
#reverse
#index
#count

a = [1, 2, 3]
print(a) #[1, 2, 3]

'''
a[3] = 4 #error IndexError: list assignment index out of range
'''
a.append(4)
print(a) #[1, 2, 3, 4]

a.insert(2, 2.5)
print(a) #[1, 2, 2.5, 3, 4]

a.insert(1, 'Name')
print(a) #[1, 'Name', 2, 2.5, 3, 4]

a = [6, 2, 8, 8, 7, 3, 9, 5, 1]
a.sort()
print(a) #[1, 2, 3, 5, 6, 7, 8, 8, 9]

fruits = ['Banana', 'Apple', 'Mango']
fruits.sort()
print(fruits) #['Apple', 'Banana', 'Mango']

a = [6, 2, 8, 8, 7, 3, 9, 5, 1]
fruits = ['Banana', 'Apple', 'Mango', 'Banana']

a.pop(0)
print(a) #[2, 8, 8, 7, 3, 9, 5, 1]

a.clear()
print(a) #[]

fruits.reverse()
print(fruits) #['Banana', 'Mango', 'Apple', 'Banana']

print(fruits.index('Apple')) #2
print(fruits.count('Banana')) #2 --> number of appearance of 'Banana'