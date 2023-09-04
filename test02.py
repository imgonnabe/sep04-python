# 딕셔너리
d = {'name': "홍길동", 'age': 120, 'home': False}
print(d)
print(type(d)) # <class 'dict'>
print(d['name'])
print(d.keys()) # dict_keys(['name', 'age', 'home'])
print(d.values()) # dict_values(['홍길동', 120, False])
print(type(d.keys())) # <class 'dict_keys'>
print("addr" in d.keys()) # False
print("age" in d.keys()) # True

d['addr'] = '서울' # 추가
print(d)
d['addr'] = '한양' # 변경
print(d)
del d['addr'] # 삭제
print(d)

# 튜플() > 수정불가
# 딕셔너리{} > key:value
# 리스트[]
# set{} > value
arr=[10,20,30,40,50]
print(type(arr)) # <class 'list'>
print(arr)
print(arr[3:])
print(arr[0])

arr.append(11)
print(arr) # [10, 20, 30, 40, 50, 11]
arr.insert(1,11) # [10, 11, 20, 30, 40, 50, 11]
print(arr)

temp=arr+[102,103]
print(temp) # [10, 11, 20, 30, 40, 50, 11, 102, 103]
arr.extend([501,502])
del arr[5]
print(arr)

arr.remove(502)
print(arr) # [10, 11, 20, 30, 40, 11, 501]

arr.reverse()
arr.sort()

# set
s={10,20,30,40,30}
print(s) # {40, 10, 20, 30}
s.add(50)
print(s) # {40, 10, 50, 20, 30}
print(type(s)) # <class 'set'>
s.update([60,70,10])
print(s) # {70, 40, 10, 50, 20, 60, 30}

s.remove(70)
print(s)

for i in s:
    print(i)

print(70 in s)
print(11 not in s)

s1=s
s.remove(40)
print(s) #{10, 50, 20, 60, 30}
print(s1) #{10, 50, 20, 60, 30}

s2=s.copy()
s.add(100)
print(s) #{100, 10, 50, 20, 60, 30}
print(s2) #{50, 20, 10, 60, 30}

print('----------------------')
a={'일본','중국','한국'}
print(a)
a.add('베트남')
a.add('중국')
print(a) #{'한국', '중국', '베트남', '일본'}
a.remove('일본')
a.update(['홍콩','한국','태국'])
print(a) #{'홍콩', '태국', '베트남', '한국', '중국'}