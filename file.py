'''
Created on 2020. 4. 8.

@author: GD7
'''
경로 = "D:/IDE/workspace-python/Python-Start/file/{0}.txt"

def start():
    print("메모장 실행")
    run = True
    while run:
        e = input("동작 선택(신규 = C , 읽기 = R , 수정 = U)")
        if e == "C" or e == "c":
            run = create(run)
        elif e == "R" or e == "r":
            run = read(run)
        elif e == "U" or e == "u":
            run = update(run)
        else:
            print("잘못입력하셨습니다.")
            continue

def read(run):
    while run:
        path = 경로.format(input("읽어야 할 대상 파일명을 입력하세요." ))
        with open(path, "r", encoding="utf8") as r:
            print(r.read())
            e = input("추가로 읽어들일 파일이 있습니까?(Y, N)")
            if e == "Y" or e == "y":
                continue
            elif e == "N" or e == "n":
                run = False
                print("종료하겠습니다.")
                break
            else:
                print("잘못입력하셨습니다.")
    return run            
                    
                        
def create(run):
    path = 경로.format(input("신규 대상 파일명을 입력하세요." ))
    with open(path, "w", encoding="utf8"):
        print("경로 : " + path + " 에 생성이 완료되었습니다.")
        print("생성된 파일이 사용가능합니다.")
        e = input("생성된 파일에 메모하시겠습니까?(Y,N) ")
        if e == "Y" or e == "y":
            print("한줄씩 입력가능합니다. (#종료 입력시 종료)")
            while run:
                txt = input()
                if txt == "#종료":
                            run = False
                            print("종료하겠습니다.")
                            break 
                with open(path, "a", encoding="utf8") as a:
                    a.write(txt + "\n")                    
        elif e == "N" or e == "n":
            print("종료하겠습니다.")
            return False
        else:
            print("잘못 입력하셨습니다.")
    return run

def update(run):
    path = 경로.format(input("수정 대상 파일명을 입력하세요." ))
    with open(path, "a", encoding="utf8") as a:
        print("수정하고자 하는 파일에 있습니다.")
        e = input("추가 메모하시겠습니까?(Y,N) ")
        if e == "Y" or e == "y":
            print("한줄씩 입력가능합니다. (#수정종료 입력시 종료)")
            while run:
                txt = input()
                if txt == "#수정종료":
                    run = False
                    print("종료하겠습니다.")
                    break
                with open(path, "a", encoding="utf8") as a:
                    a.write(txt + "\n")
        elif e == "N" or e == "n":
            print("종료하겠습니다.")
            return False   
        else:
            print("잘못 입력하셨습니다.")
    return run         
#===============================================================================
# def 메모추가(run,path):
#     print("한줄씩 입력가능합니다. (#종료 입력시 종료)")
#     while run:
#         txt = input()
#         if txt == "#종료":
#             run = False
#             break 
#             with open(path, "a", encoding="utf8") as a:
#                 a.write(txt + "\n")
#===============================================================================     