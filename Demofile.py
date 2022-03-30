#demofile.py

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("==약간 서식을 변경==")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).rjust(5))

for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(5))


#문자열 결함 연산
url = "http://www.credu.com/?page=" + str(1)
print(url)

print("--서식문자--")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(10))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(1500000))

#파일에 쓰기
f = open(r"c:\Work\demo.txt", "wt", encoding="utf-8")
f.write("한글데이터\nabcd\n1234\n")
f.close()
print(f.closed)

f = open(r"c:\Work\demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
print("어디쯤:",f.tell())

f.seek(0)
result = f.readlines()
print(result)

f.close()

#with 구문을 사용(블럭안에서만 리소스를 사용)
with open(r"c:\Work\demo.txt","rt",encoding="utf-8") as f:
    for item in f.readline():
        print(item)


