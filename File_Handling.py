#File is a named location on disk to store related information. It is used to permanently
#store data in a non-volatile memory (e.g., hard disk)
''' In Pytho, a file operation takes place in following order:
1   Open a file
2   Read or Write (perform operation)
3   Close the file'''

#How to open a file?
''' Python has a built-in function open() to open files. This function returns a file object
We can specify the mode while opening a file. In mode, we specify whether we want to read 'r'
, write 'w' or append 'a' to the file. We also specify if we want to open the file in text mode
or binary mode.

We can also use with statement instead of open() and close()
with open('filename.txt', 'w') as fileObject:
'''

f = open('data.txt', 'r')

#print(f.readline())
#print(f.readline())

#for line in f:
#    print(line)

f.close()

''' with open('data.txt') as f:
#    for line in f:
#        print(line) 

    print(f.read())
'''

#Writing to a file
''' Open the file using 'w' mode. We get a fileObject that can be used to write string into the file.
    fileObject.write(string)
    fileObject.writeline(sequences)
'''

lines_data = ['Sayoni\n', 'Rounak\n', 'Upasana\n']

with open('new_file.txt', 'w') as f:
    f.write('Vatsal\n') #writes data to the files. Truncates already existing data
    f.writelines(lines_data) #writes data to the files. Truncates already existing data
    
with open('new_file.txt', 'a') as f:
    f.write('Another_name\n') #for appending to already existing data