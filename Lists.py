# a list is created by placing all the items (elements) inside a square bracket [], separated by commas.
# list is heterogenous in nature

my_list = [1, 2, "string1", "string2"]
print(my_list) #[1, 2, 'string1', 'string2']

my_list = ["Apple", "Orange", "Mango"]
print(my_list[-1]) #Mango
my_list[1] = "Guava"
print(my_list) #['Apple', 'Guava', 'Mango']
del my_list[0]
print(my_list) #['Guava', 'Mango']

numbers = [0,1,2,3,4,5,6,7]
print(numbers[2:5]) #[2, 3, 4]
print(numbers[::-1]) #[7, 6, 5, 4, 3, 2, 1, 0]
print(numbers[-1:0:-2 ]) #[7, 5, 3, 1]

#List comprehension
a = [x for x in range(20)]
print(a) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

a = [x for x in range(20) if x%2 == 0] #even numbers
print(a) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

b = [3 ** i for i in range(5)] #3 ^ i
print(b) #[1, 3, 9, 27, 81]