'''
### 그래프 그리기

# 간단한 그래프 그리기 : 직선 그래프
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show()


# 곡선 그래프 그리기
import matplotlib.pyplot as plt
x = range(0, 100)
y = [v*v for v in x]
plt.plot(x, y)
plt.show()


# 곡선 그래프 그리기 (도트로 표현하기)
import matplotlib.pyplot as plt
x = range(0, 100)
y = [v*v for v in x]
plt.plot(x, y, 'ro')
plt.show()
'''
'''
마커 패턴으로는 ‘--', ‘s’, ‘^’, ‘+’ 등이 있습니다.
예를 들어 ‘r--'는 빨간색 대쉬라인을 의미하고, ‘
bs’는 파란색 사각형,
‘g^’는 녹색 삼각형,
‘g+’는 녹색 십자 모양을 의미합니다
'''
'''
# 한 화면에 여러개의 그래프 그리기
# 2개의 행의 그래프 그리기기
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
plt.show()


# 2개의 열의 그래프 그리기기
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
plt.show()


# Sine과 Cosine 그래프 그리기
import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0.0, 5.0, 0.1)
np.pi
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(t, np.sin(2*np.pi*t), 'b--')
ax2.plot(t, np.cos(2*np.pi*t), 'r--')
plt.show()


# 라벨 표시 하기
import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0.0, 5.0, 0.1)
np.pi
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(t, np.sin(2*np.pi*t), 'b--')
ax2.plot(t, np.cos(2*np.pi*t), 'r--')
ax1.set_xlabel('t')                   # x축의 라벨 표시
ax1.set_ylabel('sin(2*pi*t)')         # y축의 라벨 표시
ax2.set_xlabel('t')                   # x축의 라벨 표시
ax2.set_ylabel('cos(2*pi*t)')         # y축의 라벨 표시
plt.show()



#범례 추가 하기
import pandas_datareader.data as web
lg = web.DataReader("066570.KS", "yahoo")
samsung = web.DataReader("005930.KS", "yahoo")

import matplotlib.pyplot as plt
plt.plot(lg.index, lg['Adj Close'], label='LG Electronics')  # 범례 추가
plt.plot(samsung.index, samsung['Adj Close'], label='Samsung Electronics') # 범례 추가
plt.legend(loc='upper left')                                       # 범례 위치 설정
plt.show()

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

'''


