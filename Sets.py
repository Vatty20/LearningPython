a = {1, 2, 3, 5, 6, 3, 1}
print(a) #{1, 2, 3, 5, 6}
         #elements are not repeated
'''
print(a[0]) #TypeError: 'set' object is not subscriptable
            #Elements in sets are not stored in any order, but randomly
'''            
for elements in a:
    print(elements * 2) #2
                        #4
                        #6
                        #10
                        #12
                        
