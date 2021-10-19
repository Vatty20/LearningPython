#for loop 
'''
for x in range(10):
    print(2 * x, end = ", ") #0, 2, 4, 6, 8, 10, 12, 14, 16, 18,

print()
a = ['Vatsal', 'Sayoni', 'Rounak']
for name in a:
    print(name) #Vatsal
                #Sayoni
                #Rounak
    
for name in a:
    print(name*2) #VatsalVatsal
                  #SayoniSayoni
                  #RounakRounak
'''
#while loop
'''
n = int(input()) #6
while n >= 0:
    print(n, end = " ") #6 5 4 3 2 1 0
    n -= 1
'''
#using break
for n in range(10):
    if n > 5:
        break 
    print(n, end = " ") #0 1 2 3 4 5 
    
print()
#using continue
for n in range(10):
    if n == 3:
        continue 
    print(n, end = " ") #0 1 2 4 5 6 7 8 9