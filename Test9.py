'''
Created on 2020. 4. 8.

@author: GD7
'''
def 연산(int_a,t,int_b,r):
    if t == "+":
        r = int_a + int_b
    elif t == "-":
        r = int_a + int_b
    elif t == "/":
        r = int_a + int_b
    elif t == "*":
        r = int_a + int_b
    else:
        return True
    print(int_a, t, int_b,"=",r)
    return False

def 동작(e1):
    while True:
        e = input("계속진행하시겠습니까?(Y,N) ")
        if e == "N" or e == "n":
            e1 = False
            print("종료")
        elif e == "Y" or e == "y":
            pass
        else:
            continue
        break
    return e1

import Test8 as calc
calc.시작()
