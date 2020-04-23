#!python
print("Content-Type: text/html; charset=utf-8\n\n")
import cgi, DB as db
params = cgi.FieldStorage()
#f = open("files/" + params["title"].value, "w", encoding="UTF8")
#f.write(params["content"].value)
#f.close()

#insert
sql = "INSERT INTO list (`title`, `content`) VALUES (%s, %s)"
cnt = db.insert(sql,[params["title"].value, params["content"].value])

print(cnt)

