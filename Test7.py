'''
Created on 2020. 4. 7.

@author: GD7
'''
fp = "D:/IDE/workspace-python/Python-Start/blank.txt"
#===============================================================================
# #파일읽기
# file = open(fp, "r", encoding="utf8") # "r" = read
# print(file)
# print(file.read())
# print(type(file))
# file.close() # io 정상정료
#===============================================================================

#===============================================================================
# with open(fp, "r", encoding="utf8") as f:
#     print(type(f))
#     print(f.read())
#     print(type(f.read()))
#     # with 는 close 자동실행 , as 변수화(별명)
#===============================================================================

#===============================================================================
# #var = "\na='내용'"
# 파일 = input("생성할 파일명을 입력하세요.")
# 파일경로  ="D:/IDE/workspace-python/Python-Start/{0}.txt".format(파일)
# 파일객체 =open(파일경로,"w",encoding="utf8")
# 파일객체.close()
# for i in range(10):
#     txt = input()
#     with open(파일경로, "a", encoding="utf8") as f:
#         f.write(str(i) + "\t" + txt + "\n")
#===============================================================================

파일경로 = "D:/IDE/workspace-python/Python-Start/{0}.txt".format(input("생성할 파일명을 입력하세요."))
for i in range(10):
    txt = input()
    with open(파일경로, "a", encoding="utf8") as f:
        f.write(txt + "\n")
