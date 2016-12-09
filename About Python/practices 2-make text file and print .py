'''
문제 7-1

1부터 10까지의 숫자를 각 라인 단위로 파일에 출력하는 프로그램을 작성하세요.

생성되는 파일의 이름은 number.txt 이다.

문제 7-2

사용자로부터 경로를 입력 받은 후 해당 경로에 있는 디렉터리와 파일 목록을 flist.txt라는 파일로 출력하는 함수를 작성하세요.

'''
## 문제 7-1

# number.txt 파일 생성
file_number = open('C:\\Users\\jongguk\\PycharmProjects\\Python-for-Trading\\number.txt', 'wt')

'''
# way 1 :
file_number.write(" 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n 10\n")

# way 2:
for i in range(1,11)
    file_number.writhe ("%d\n" % i)


file_number.close()
'''
# 문제 7-2
# 문제 7 answer:
import os
def print_flist(path):
    f= open('C:\\Users\\jongguk\\PycharmProjects\\Python-for-Trading\\file_list.txt', 'wt')
    flist = os.listdir(path)                  # 해당 폴더의 리스트를 볼수있는 명령어
    for x in flist:
        f.write('%s\n' % x)
    f.close()
print_flist('C:\\Users\\jongguk\\PycharmProjects\\Python-for-Trading')   # 리스트 확인 경로 입력

'''
## 기능 추가
 - 폴더의 경로를 입력 받고  해당 경로가 존재하면 리스트 출력
 - 존재하지 않으면 에러 메시지 출력

import os
input_path = input("This folder list is :  ")

def print_flist(path):
    file_list = open('C:\\Users\\jongguk\\PycharmProjects\\Python-for-Trading\\file_list.txt', 'wt')
    flist = os.listdir(path)                  # 해당 폴더의 리스트를 볼수있는 명령어
    for x in flist:
        file_list.write('%s\n' % x)
    file_list.close()
print_flist('c:\\Anaconda3')

'''






















