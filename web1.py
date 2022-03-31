# web1.py

from bs4 import BeautifulSoup


#문서를 로딩(문서 전체를 읽어서 문자열로 리턴)
page = open("c:\\Work\\test01.html","rt",encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#전체 문서를 보기
#print(soup.prettify())

#문서에 있는 <p> 태그를 전부 가져오기
# print(soup.find("p"))

# print(soup.find_all(id="first"))

#태그 내부에 있는 문자열 출력
for tag in soup.find_all("p"):
    content = tag.text.strip()
    content = content.replace("\n", "")
    content = content.replace("\t", "")
    content = content.replace("  ", "")
    print(content)





