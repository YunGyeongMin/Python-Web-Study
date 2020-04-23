'''
Created on 2020. 4. 7.

@author: GD7
'''

배열 = ['문자', 1, 0.5, False]
print(배열)
for i in 배열:
    print(i)
    
#-추가
입력 = input("추가값 입력하세요 > ")
#배열[1] = 입력
배열.append(입력)
print(배열)

#-읽기
print(배열[2])

#-삭제
배열.remove(입력)
print(배열)

del 배열[2]
print(배열)
#-변경
배열[2] = "변경"
print(배열) 