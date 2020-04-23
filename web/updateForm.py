#!python
print("Content-Type: text/html; charset=utf-8\n\n")
import cgi, os, DB as db
params = cgi.FieldStorage()
#num = int(params["num"].value) - 1
#content = params["content"].value
#list = os.listdir("files")
#f = open("files/" +list[num], "w", encoding="utf8")
#f.write(content)
#f.close()

sql = "UPDATE `list` SET  `content` = %s WHERE `no` = %s"
db.update(sql, [params["content"].value , int(params["num"].value)])

print(1)