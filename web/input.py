#!python
print("Content-Type: text/html; charset=utf-8\n\n")

import cgi

data = cgi.FieldStorage();
print(data["txt"].value)

with open("params.txt", "a", encoding="utf8") as f:
    f.write(data["txt"].value + "\n")
    
html = '''
<html>
    <meta http-equiv="refresh" content="0; url=/index.py"></meta>
</html>
'''
print(html)