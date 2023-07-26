# DemoRe.py

import re

# 숫자가 0에서 N번th
# 함정을 추가
result = re.search("[0-9]*th", "   35th")  # 찾는 패턴, 주어진 문자열
print(result)
print(result.group())

# 선택한 블록 주석처기 : ctrl + /
# 정확하게 일치하는 패턴 찾기
# 못찾으면 중지
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())


result = re.search("apple", "빅테크에서 apple의 위상")
print(result.group())
result = re.search("\d{4}", "올해는 2023년")        # 4자리 연속된 숫자
print(result.group())
result = re.search("\d{5}", "우리 동네는 42300")    # 5자리 연속된 숫자
print(result.group())

print("-----대소문자-----")
data = "Apple is big company and apple is very delicious"
c = re.compile("apple", re.IGNORECASE)      # 대소문자 무시
print(c.findall(data))                      # 하나가 아니라 있는거 전부 찾기

print("-----다중라인검색-----")
data2 = """파이썬을
배워서


누구나 사용
"""
# 다중라인. 비어있는 줄은 제외하고 데이터 가져오기
c = re.compile("^.+", re.MULTILINE)         # (^)시작패턴 지정. (.)문자. (+)1개 이상.
print(c.findall(data2))
