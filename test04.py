class good:
    li = ['서울', '경기', '인천', '대전', '부산']


g = good()
str01 = ''
for i in g.li:
    str01 = str01 + i[0]

print(str01)
