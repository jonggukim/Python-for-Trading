'''
## Pandas Series

# 튜플 - 데이터의 내용을 수정할 수가 없다.

#  리스트
mystock = ['kakao', 'naver']
print(mystock[0])
print(mystock[1])

for stock in mystock:
    print(stock)

# 딕셔너리
exam_dic = {'key1': 'room1', 'key2':'room2'}
print(exam_dic['key1'])
print(exam_dic['key2'])


# 리스트로 구현
kakao_daily_ending_prices = [92300, 94300, 92100, 92400, 92600]
for price in kakao_daily_ending_prices:
    print(price)

# 딕셔너리를 사용하여 구현
kakao_daily_ending_prices = {'2016-02-19': 92600,
                             '2016-02-18': 92400,
                             '2016-02-17': 92100,
                             '2016-02-16': 94300,
                             '2016-02-15': 92300}
print(kakao_daily_ending_prices['2016-02-19'])




from pandas import Series, DataFrame

raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data = DataFrame(raw_data)
print(data)
'''



Location String	Location Code
‘best’	0
‘upper right’	1
‘upper left’	2
‘lower left’	3
‘lower right’	4
‘right’	5
‘center left’	6
‘center right’	7
‘lower center’	8
‘upper center’	9
‘center’	10





























