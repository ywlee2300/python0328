#DemoDict.py



def calc(a,b):
    return a+b, a*b

result = calc(3,4)



print(result[0])
print(result[1])

argc = (5,6)

print(calc(*argc)[0])


a= set((1,2,3))
print(a)
print(type(a))

b=list(a)
print(b)
b.append(5)
print(b)
c=(1,2,3)
print(type(c))


#dictionaly

d = {"apple":"red", "kiwi":"green"}
print(len(d))
print(d["apple"])
d["banana"]="yellow"
print(d)

device = {"아마존":5, "아이패드":10, "윈도우":20}
device["맥"]=15
print(device)
device["아이폰"]=6
print(device)
del device["아이폰"]
print(device)

mydevice=device

print(id(device))

print(id(mydevice))

del mydevice["아마존"]
print(device)