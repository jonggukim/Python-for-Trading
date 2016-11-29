'''
# 파일 데이터 읽기




# 파일을 열고 데이터 읽기 : rt >>> 존재하는 파일을 읽는다
f = open('C:\\Users\\jongguk\\PycharmProjects\\Python-for-Trading\\test.txt', 'rt')
lines = f.readlines()
print(lines)

# 데이터의 표현 및 출력
for line in lines:
    print(line, end="")

# 데이터의 표현 및 출력
for line in lines:
    nline = line.split('\n')[0]
    print (nline)


'''
# 데이터 파일 쓰기: wt >>> 파일을 생성하고 (파일이 존재하지 않으면) 쓰기 가능 상태로 한다.
f1 = open('C:\\Users\\jongguk\\PycharmProjects\\Python-for-Trading\\write1.txt', 'wt')
f2 = open('C:\\Users\\jongguk\\PycharmProjects\\Python-for-Trading\\write.txt', 'wt')

# 데이터의 추가 : write1.txt 파일에 내용을 쓴다. >> 추가가 아닌 새로 쓰기임 기존 데이터 삭제.

f1.write('this is first line for writing\n')
f1.write('test line for writing \n')
f1.close()
f2.write(' 111111 \n 222222222\n 33333333\n')
f2.close()


























