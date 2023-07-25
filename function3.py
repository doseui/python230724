# function3.py

# 가변인자
def union(*ar):
    # 지역변수 리스트
    result = []
    for item in ar:     # 단어 단위로 나누기
        for x in item:  # 문자 단위로 나누기
            if x not in result:
                result.append(x)
    return result


# 호출
print( union("HAM", "SPAM"))
print( union("HAM", "SPAM", "EGG"))
