#!python
print("Content-Type: text/json; charset=utf-8\n\n")

import pymysql

# pip 를 이용하여 pymysql
'''
    pip install pymysql                      < 패키지 설치
    pip freeze > package.txt                 < 설치된 목록 확인 
    pip uninstall -r package.txt -y          < 패키지 목록 대상 삭제
'''

conn = pymysql.connect(host="192.168.3.209",port=3306,user="gudi", password="1234", db="Python", charset="utf8") # DB연결정보
cur = conn.cursor(pymysql.cursors.DictCursor) #DB연결 , 컬럼명은 나오지않고 컬럼의 순서는 지켜줌 , # pymysql.cursors.DictCursor=컬럼명과 데이터 - > 키,밸류형식으로 가져온다.


sql = "INSERT INTO test (num, txt) VALUES (%s,%s);"
cur.execute(sql, (8,'팔')) #쿼리문 실행
conn.commit() #데이터저장


sql = "SELECT num, txt FROM test"
cur.execute(sql) #쿼리문 실행
row = cur.fetchall()

#row = cur.fetchall() # 전체row 가져오기
#row = cur.fetchone() # row 하나만 가져오기

print(row)

print("===================")
sql += " where num = %s"
cur.execute(sql, (2))
row = cur.fetchone()
print(row)

conn.close()