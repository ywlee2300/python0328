# db1.py

import sqlite3

#전역함수로 연결객체 리턴(파일을 영구적으로 저장)
con = sqlite3.connect("c:\\Work\\sample.db")
#두번째 인스턴스면 커서를 리턴받기
cur=con.cursor()
#테이블을 가장 먼저 생성
cur.execute("create table PhoneBook (name text, phoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")
cur.execute("insert into PhoneBook values ('mathew', '010-111');")
cur.execute("insert into PhoneBook values ('marc', '010-112');")
cur.execute("insert into PhoneBook values ('tom', '010-122');")

name = "lee"
phonenumber = "010-123"

cur.execute("insert into PhoneBook values (?, ?);", (name, phonenumber))

#검색하기
# cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)
cur.execute("select * from PhoneBook;")

# print("--fetchone()--")
# print(cur.fetchone())
# print("--fetchmany(2)--")
# print(cur.fetchmany(2))
print("--fetchall()--")
print(cur.fetchall())

con.commit()