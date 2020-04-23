#!python
print("Content-Type: text/html; charset=utf-8\n\n")

import cgi

def get(parameter):
    if "var" in parameter:
        old = open("data.txt", "r", encoding="utf8").read()
        # print(type(old))
        if "a" == parameter["var"].value :
            var = old + " + "
            with open("data.txt", "w", encoding="utf8") as f:
                f.write(var)
        elif "b" == parameter["var"].value :
            var = old + " - "
            with open("data.txt", "w", encoding="utf8") as f:
                f.write(var)
        elif "c" == parameter["var"].value :
            t = old.split(" ")
            with open("data.txt", "w", encoding="utf8") as f:
                f.write("0")
            if "+" == t[1]:
                return int(t[0]) + int(t[2])
            elif "-" == t[1]:
                return int(t[0]) - int(t[2])
        else:
            new = parameter["var"].value
            # print(type(new))
            var = 0
            if "0" == old:
                var = new
            else:
                var = (old + new)
            with open("data.txt", "w", encoding="utf8") as f:
                f.write(var)
            return var 
        return old
    return 0

with open("views/ex1.html", "r", encoding="utf8") as f:
    print(f.read())

html = '''
    <section>
        <form>
            <input type="text" name="result" readonly="readonly" value="{0}">
            <input type="hidden" name="var">
        </form>
    </section>
    <section class="body">
        <ul>
            <li><a href="?var=7">7</a></li>
            <li><a href="?var=8">8</a></li>
            <li><a href="?var=9">9</a></li>
            <li><a href="?var=a">+</a></li>
            <li><a href="?var=4">4</a></li>
            <li><a href="?var=5">5</a></li>
            <li><a href="?var=6">6</a></li>
            <li><a href="?var=b">-</a></li>
            <li><a href="?var=1">1</a></li>
            <li><a href="?var=2">2</a></li>
            <li><a href="?var=3">3</a></li>
            <li><a href="?var=c">=</a></li>
        </ul>
    </section> 
'''.format(get(cgi.FieldStorage()))
print(html)
