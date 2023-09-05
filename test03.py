lol=[[1,2,3],[4,5],[6,7,8,9]]
print(lol[0])
print(lol[2][1]) # 7
for sub in lol:
    for item in sub:
        print(item, end='')
    print()
# 123
# 45
# 6789

def exam(num1,num2=2):
    print('a=', num1, 'b=', num2) #a= 20 b= 2 :,에 공백이 들어간다.

exam(20)

class Pass:
    def byPass(self):
        print("pass")


p=Pass()