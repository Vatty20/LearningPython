#isalpha() --> checks if string has all alphabets

s1 = 'abcd'
print(s1.isalpha()) #True
s1 = 'abcd123'
print(s1.isalpha()) #False

#isdigit()

s2 = '123'
print(s2.isdigit()) #True
s2 = '123a'
print(s2.isdigit()) #False

#islower()
#lower()
#upper()
#isupper()
#lstrip() --> reduces extra blank spaces from left of string
#rstrip() --> reduces extra blank spaces from right of string

s = 'abcde'
print('s.isalpha', s.isalpha()) #s.isalpha True
print('s.isdigit', s.isdigit()) #s.isdigit False
print('s.islower', s.islower()) #s.islower True
print('s.isupper', s.isupper()) #s.isupper False
print('s.lower', s.lower()) #s.lower abcde
print('s.upper', s.upper()) #s.upper ABCDE