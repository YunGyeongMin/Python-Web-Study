#!python
print("Content-Type: text/html; charset=utf-8\n\n")

#import DB as db

with open("views/list.html", "r", encoding="utf8") as f:
    print(f.read())

#sql2 = "SELECT num, txt FROM test"
#list.selectList(sql2, {})
#print(list)