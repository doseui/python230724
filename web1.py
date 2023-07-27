# web1.py

# 크롤링을 하기 위한 선언
from bs4 import BeautifulSoup

# 페이지를 로딩
# page = open("C:/work/test01.html", "rt" encodings="utf-8")
# page = page.read()

# 함수를 연속으로 부를 때 사용. 두 줄을 한줄로 사용
page = open("C:/work/test01.html", "rt", encoding="utf-8").read()

# 검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")

# 페이지 보기
# print(soup.prettify())

# <p> 전체를 검색. p태그
# print(soup.find_all("p"))   # <p>에서 꺽쇠는 생략해도 됨

# <p> 태그 하나를 검색
# print(soup.find("p"))


# < class='outer=text'> 조건 검색
# print(soup.find_all("p", class_="outer-text")) # _하나 붙이는 이유 : 파이썬의 키워드와 충돌방지 위해

# attrs:Attributes(속성등)
# print(soup.find_all("p", attrs={"class":"outer-text"}))

# id=first
# print(soup.find_all(id="first"))

# 태그 내부 문자열 가져오기(.text속성)
for tag in soup.find_all("p"):
    title = tag.text.strip()    # 태그는 제외하고 텍스트만 가져오기 -> 공백문자 제거
    title = title.replace("\n", "") # 줄바꿈 제거
    print(title)

