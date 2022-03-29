#function3.py

#가변인자
from tkinter import Y


def union(*ar):
    #지역변수를 리스트로 초기화
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result


print(union("ABC", "CDE","ASEF"))
print(union("HAM","BUR","GER"))

#정의되지 않은 인자
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL
print(userURIBuilder("credu.com", "80", id="kim", age="30"))
print(userURIBuilder("credu.com", "80", id="kim", age="30", name="mike"))

g = lambda x,y:x*y
print(g(2,3))