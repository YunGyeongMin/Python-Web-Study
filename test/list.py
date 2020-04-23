#!python
print("Content-Type: text/html; charset=utf-8\n\n")

import cgi, os

parameter = cgi.FieldStorage()
folder = os.listdir("list2")   

li=""
for result in folder:
         if "title" in parameter:
             if result.find((parameter["title"].value) > -1):
                  li += '''
                    <li class="row">
                        <div class="col1">1</div>
                        <div class="col2">제목</div>
                    </li>
                '''.format(result)
            else:
                li += '''
                    <li class="row">
                        <div class="col1">1</div>
                        <div class="col2">제목</div>
                    </li>
                '''.format(result)





with open("views/list.html", "r", encoding="utf8") as f:
    print(f.read())

    
html = '''
    <section>
        <h1 class="header">게시판</h1>
        <div class="buttons">
            <button type="button"><a href="/write.py">작성하기</a></button>
        </div>
        <ul class="body">
           {0}
        </ul>
    </section>
'''

print(html)    