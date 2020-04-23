'''
Created on 2020. 3. 31.

@author: GD7
'''

a = 2
if a == 4 | a == 1: 
    print("참")
    a = False 
    print(a)
elif a == 2:
    print("elif")
    print("a = {0}".format(a))    
else:
    a = True
    print("1")
print(a)    
    