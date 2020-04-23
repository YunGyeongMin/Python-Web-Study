#!python
print("Content-Type: text/html; charset=utf-8\n\n")
import cgi, os, DB as db
params = cgi.FieldStorage()
num = int(params["num"].value) - 1
list = os.listdir("files")
os.remove("files/" + list[num])

sql = "UPDATE `list` SET  `delYn` = 'Y' WHERE `no` = %s"
db.update(sql,int(params["num"].value))

html = '''
<meta http-equiv="refresh" content="0;url=list.py">
'''
print(html)
