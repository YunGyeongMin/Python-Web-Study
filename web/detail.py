#!python
print("Content-Type: text/html; charset=utf-8\n\n")

with open("views/detail.html", "r", encoding="utf8") as f:
    print(f.read())
