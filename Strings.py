#name = 'Vatsal'
#multi_line = '''This
#is
#a
#multi 
#line
#string'''
#print(name)
#print(multi_line)

'''
fruit = 'Apple'
print(fruit[0]) #A
print(fruit[3]) #l
#print(fruit[5]) #IndexError: string index out of range
print(fruit[-1]) #e
print(fruit[-3]) #p
'''

#slicing --> subsequence of string, doesn't alter original string
'''
s = 'abcde'
print(s[1:4]) #bcd
print(s[1:5]) #bcde
print(s[:4]) #abcd
print(s[2:]) #cde
print(s[0:5:2]) #ace --> skips 1 character from beginning

#printing in reverse
print(s[::-1]) #edcba
print(s[-1:0:-1]) #edcb (starts with last index [-1] to first index [0] and takes 1 step back [-1])
'''

#concatenation
a = 'abc'
b = 'def'
c = a+b
print(c) #abcdef
print(a+b) #abcdef

#using for in Strings

s = 'abcd'
for s1 in s:
    print(s1*3) #aaa
                #bbb
                #ccc
                #ddd
