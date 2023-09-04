print("파이참")
a=(100,200,400,"hi",False)
b= a+(500,600)
print(b)
print(b[3:])
# str[시작:끝:(스텝)]
s="가나다라마바사"
print(s[1:2])
print(s[-1]) # 사
print(s[-1:-5])
print(s[-3:]) # 마바사
print(s[-3:2])

print("----------------")
a="remember november"
b=a[:3]+a[12:15] # rem emb
c="r and %s" %"str"
print(b) # rememb
print(c) # r and str
print(b+c) # remembr and str
print('hi')