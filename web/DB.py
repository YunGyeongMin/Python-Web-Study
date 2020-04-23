import pymysql

# pip 를 이용하여 pymysql
'''
    pip install pymysql                      < 패키지 설치
    pip freeze > package.txt                 < 설치된 목록 확인 
    pip uninstall -r package.txt -y          < 패키지 목록 대상 삭제
'''

#row = cur.fetchall() # 전체row 가져오기
#row = cur.fetchone() # row 하나만 가져오기

def con():
    return pymysql.connect(host="192.168.3.209",port=3306,user="gudi", password="1234", db="Python", charset="utf8") # DB연결정보
    

#sql1 = "INSERT INTO test (num, txt) VALUES (%s,%s);"
#sql2 = "SELECT num, txt FROM test"
#sql3 = sql2 + " where num in (%s,%s)"
#sql3 = sql2 + " where num = %s"


def insert(sql, params):
    conn = con()
    count = 0
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(sql, params) #쿼리문 실행
    finally:    
        conn.commit() #데이터저장
        conn.close()
    return count   

def update(sql, params):
    conn = con()
    count = 0
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(sql, params) #쿼리문 실행
    finally:    
        conn.commit() #데이터저장
        conn.close()
    return count 

def selectList(sql, params):
    conn = con()
    row = []
    try:
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(sql, params) #쿼리문 실행
        row = cur.fetchall()
    finally:
        conn.close()
    return row

def selectOne(sql, params):
    conn = con()
    row = {}
    try:
        cur = conn.cursor(pymysql.cursors.DictCursor)    
        cur.execute(sql, params)
        row = cur.fetchone()
    finally:
        conn.close()    
    return row

#print(selectList(sql2, {}))
#print(selectList(sql3, [2,3]))

#v = []
#v.append(2)
#v.append(3)
#print(selectList(sql3, v))

#e = {"col1" : 2, "col2": 3}
#print(selectList(sql3, e))