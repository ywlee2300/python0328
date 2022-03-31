# web2.py
# 웹서버와 통신할 경우 사용
import urllib.request
#크롤링에 사용
from bs4 import BeautifulSoup


address = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri&page="
f = open("c:\\Work\\webtoon.txt", "wt", encoding="utf-8")
for k in range(1,6):
    data = urllib.request.urlopen(address+str(k))
    soup = BeautifulSoup(data, "html.parser")
    #블럭 주석: ctrl + / 
    # <td class="title">
    #     <a href="/webtoon/detail?titleId=20853">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
    # </td>

    cartoons = soup.find_all("td", class_="title")
    print("개수:{0}".format(len(cartoons)))



    for i in range(len(cartoons)):
        title = cartoons[i].find("a").text
        link = cartoons[i].find("a")["href"]
        print(title)
        print(link)
        f.write(title + "\n")
        f.write(link + "\n")

f.close()
print("크롤링 작업 종료")

# f = open("c:\\Work\\webtoon.txt", "wt", encoding="utf-8")
# for item in cartoons:
#     title = item.text.strip()
#     print(title)
#     f.write(title + "\n")

# f.close()
# print("크롤링 작업 종료")

# for item in cartoons:
#     title = item.text.strip()
#     print(title)