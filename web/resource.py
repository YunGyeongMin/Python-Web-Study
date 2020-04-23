#!python
print("Content-Type: text/json; charset=utf-8\n\n")

import json, os, DB as db
#list = os.listdir("files")

sql = "SELECT no, title, content FROM list WHERE delYn = %(delYn)s"
params = {"delYn" : "N"}
result = db.selectList(sql, params)
#for file in list :
#    row = {}
#    row["title"] = file
#    f = open("files/" + file, "r", encoding="UTF8")
#    row["content"] = f.read()
#    f.close()
#    result.append(row)

print(json.dumps(result, separators=(",", ":"), ensure_ascii=False))