import pandas as pd

data = pd.DataFrame(
    [[15, '남', '남중'], [17, '여', '여중']],
    index=['철수', '영희'],
    columns=['나이', '성별', '학교']
)
print(data)
data.drop(['성별', '학교'], axis=1, inplace=True)
print(data)