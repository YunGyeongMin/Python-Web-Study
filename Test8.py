'''
Created on 2020. 4. 8.

@author: GD7
'''
'''
def a():
    print("실행")
    return "A"

print(1)
print(a())
print(2)
'''
'''
def b(a,b):
    return a + b

print(b(1,int(input())))
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
        e = input("동작하시겠습니까? (Y,N 입력해주세요) ")
        if e == "N" or e == "n":
            e1 = False
            print("종료")
        elif e == "Y" or e == "y":
            pass
        else:
            continue
        break
    return e1

def 시작():
    while 동작(True):    
        if 연산(int(input("첫번째 숫자입력")),input("연산자 입력"),int(input("두번째 숫자입력")),0):
            print("잘못된 연산기호 입니다.(+,-,*,/ 중에 입력하세요)")
            continue
    
   
    

