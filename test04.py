class good:
    li = ['서울', '경기', '인천', '대전', '부산']


g = good()
str01 = ''
for i in g.li:
    str01 = str01 + i[0]

print(str01)

a = "REMEMBER NOVEMBER"
b = a[:3] + a[12:15]
c = "R AND %s" %"STR"
print(b+c)

a, b = 100, 200
print(a == b)

def exam(num1, num2=2):
    print('a=', num1, 'b=',num2)

exam(20)

lol = [[1,2,3],[4,5],[6,7,8,9]]
for sub in lol:
    for item in sub:
        print(item, end="")
    print()

for i in range(1,11,2):
    print(i, end="")