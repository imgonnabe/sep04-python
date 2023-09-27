import pandas as pd
numbers = [1,2,3]
nums = pd.Series(numbers)
print(nums)
print(12/3)

a=100
result=0
for i in range(1,3):
    result=a>>i
    print(bin(result))
    result=result+1
    print(bin(result))
    print(result)
print(result)

a=[1,2,3]
b=a.copy()
c=a
b.extend([5])
c.extend([4])

print(a) #[1, 2, 3, 4]
print(b) #[1, 2, 3, 5]
print(c) #[1, 2, 3, 4]

print(hex(id(a)))#0x2c4f566e7c0
print(hex(id(b)))#0x2c4e8d87000
print(hex(id(c)))#0x2c4f566e7c0
