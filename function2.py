#function2.py

#함수 내부의 이름을 해석하는 규칙 (LGB) Local --> Global --> Built-in


#전역변수

from asyncio.windows_events import NULL


x=2

#함수의 정의

def func(a):
    return a+x

#호출
print(func(1))

#함수정의

def func2(a):
    x=5
    return a+x

#호출
print(func2(1))

#기본값이 있는 경우
def times(a=10, b=20):
    return a*b

print(times())
print(times(b=5))
print(times(5,6))

def connectURI(server, port):
    strURL="http://"+server+":"+port
    return strURL

print(connectURI("credu.com","80"))
print(connectURI(port="80",server="credu.com"))