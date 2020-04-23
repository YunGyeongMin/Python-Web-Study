#!python
print("Content-Type: text/html; charset=utf-8\n\n")

import cgi, os #os 운영체제관련

parameter = cgi.FieldStorage()
folder = os.listdir("list") #디렉토리 설정후 목록가져오기

li = ""
for file in folder :
    #print(file + "<br>")
    if "result" in parameter:
        if file.find((parameter["result"].value)) > -1:
            li += '''
            <li>{0}</li>
            '''.format(file)
    else:
        li += '''
            <li>{0}</li>
            '''.format(file)
   

with open("views/ex2.html", "r", encoding="utf8") as f:
    print(f.read())

html = '''
<div class="body">
        <ul>
            {0}
        </ul>
</div>
'''.format(li)

print(html)