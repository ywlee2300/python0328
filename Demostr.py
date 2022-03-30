#demostr.py



print(dir(str))
test = "python is powerful".endswith("ful", 9)
print(test)

u = "<<<  spam and ham  >>>"
print(u)
print(u.strip("<> "))
print(u.rstrip("<> "))
print(u.lstrip("<> "))
print(u.replace("spam", "spam egg"))
print(u.count("spam"))
result = u.split(" ")
print(result)
print(type(result))