import pandas as pd

data=pd.DataFrame(
    [[90,89,85,100],[80,89,95,90],[70,95,100,90]],
    index=['서준','우현','인아'],
    columns=['수학','영어','음악','체육']
)
print(data)
print(data.loc[['서준', '우현']])
print(data.loc['서준'])
print(data.loc['서준':'우현'])
print(data.loc[[True,True,True]])