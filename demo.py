# demo.py
# 코드 실행 : ctrl + F5
# 터미널 보기 : ctrl + ~


a = ["red", "black", "blue"]

a += ["red"]
a.append("blue")
print(a)

a.sort()
print(a)

a = { 1, 2, 3, 3}

print(type(a))


b = (1,2,3)

print(b.index)



list = [1, 2, 3]
print(id(list))
list.append(4)
print(id(list))
import copy

demo = {"apple":"red", "kiwi":"green"}

demo2=copy.deepcopy(demo)
print(demo)
print(demo2)
print(id(demo))
print(id(demo2))
