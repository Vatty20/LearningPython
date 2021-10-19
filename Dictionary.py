#Dicitonary has a key-value pair

marks = {'Student1': 56, 'Student2': 96, 'Student3': 45}
print(marks) #{'Student1': 56, 'Student2': 96, 'Student3': 45}

print(marks['Student3']) #45

squares = {1: 1, 2: 4, 3: 9, 5: 25, 6: 36}
for i in squares:
    print(squares[i]) #1
                      #4
                      #9
                      #25
                      #36

'''
You can also update a dictionary by modifying existing key-value pair or by merging another
dictionary to an existing one.
We can add new items or change the value of existing items using assignment operator.
If the key is already present, value gets updated, else a new key:value pair is added to 
the dictionary. 
'''

marks['Student4'] = 55
print(marks) # {'Student1': 56, 'Student2': 96, 'Student3': 45, 'Student4': 55}
marks['Student2'] = 55
print(marks) # {'Student1': 56, 'Student2': 55, 'Student3': 45, 'Student4': 55}