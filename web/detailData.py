#!python
print("Content-Type: text/json; charset=utf-8\n\n")
import cgi, os, json, DB as db
param = cgi.FieldStorage()
result = {}

sql = "SELECT no, title, content FROM list WHERE delYn = 'N' AND `no` = %(no)s"
params = {"no" : param["num"].value}
result = db.selectOne(sql, params)

#num = int(params["num"].value) - 1
#list = os.listdir("files")
#content = open("files/" + list[num], "r", encoding="utf8").read()
#result = {"num": num, "title": list[num], "content": content}


print(json.dumps(result, separators=(",", ":"), ensure_ascii=False))