#!python
print("Content-Type: text/html; charset=utf-8\n\n")

import cgi
parameter = cgi.FieldStorage()

with open("views/write.html", "r", encoding="utf8") as f:
    print(f.read())

path1 ="D:/IDE/workspace-python/Python-Start/web/list2/{0}"

path2 = path1.format(parameter["title"].value)
with open(path2 , "w", encoding="utf8") as w:
    w.write(parameter["content"].value)
    
  




