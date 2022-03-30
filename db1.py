# db1.py

import sqlite3

#전역함수로 연결객체 리턴
con = sqlite3.connect(":memory:")
#두번째 인스턴스면 커서를 리턴받기
cur=con.cursor()
#테이블을 가장 먼저 생성
cur.execute("create table PhoneBook (name text, phoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")

#검색하기
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)