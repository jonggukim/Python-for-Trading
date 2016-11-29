'''
# Question: output specific directorie's information
def print_directory_contents(sPath):
    """
    This function takes the name of a directory
    and prints out the paths files within that
    directory as well as any files contained in
    contained directories.

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your
    ability to work with nested structures.
    """
    fill_this_in


Path = "C:\\Users\\jongguk\\PycharmProjects\\Python-for-Trading"

'''
# =================================================
# Answer 1: Using listdir()
'''
def print_directory_contents(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

Methods
*** main ***
    os.listdir()                 # 해당 경로 폴더의 리스트를 출력하는 함수
    os.path.join()               # 주어진 경로와 이름을 합쳐서 보여주는 함수: os.path.join(경로,파일이름)
    os.path.isdir()              # 주어진 경로의 존재를 파악하는 함수 : 존재=True, 존재하지 않음 = False
*** additionals ***
    os.path.isfile()             # 주어진 경로의 파일 존재를 파악하는 함수 : 존재=True, 존재하지 않음 = False
    os.path.exist()              # 주어진 경로의 폴더 및 파일 존재를 파악하는 함수 : 존재=True, 존재하지 않음 = False


'''
# os 모듈을 불러온다
import os
# 함수의 생성 : 주어진 폴더의 하부 폴더 및 파일 리스트를 출력하는 함수 작성
def output_dir_contents(sPath):
# 주어진 폴더경로의 하부 폴더 리스트 생성
    for sChild in os.listdir(sPath):
#생성된 리스트에 주어진 경로 path를 합친다.
        sChildPath = os.path.join(sPath,sChild)
# 주어진 경로 + 생성된 리스트를 생성해 보여준다.
#       print(sChildPath)
# 주어진 경로가 존재하면
        if os.path.isdir(sChildPath):
# 하부 경로의 검색 : 주어진 경로 + (주어진 경로 + 리스트 ).... >>> 최종경로까지 반복
            output_dir_contents(sChildPath)
# 더이상 하부 경로가 존재하지 않으면
        else:
# 결과값 출력 >>> 주어진 폴더 아래의  파일들의 최종 경로 표시.
            print(sChildPath)
#
test = output_dir_contents("C:\\Users\\jongguk\\PycharmProjects\\Python-for-Trading")
print ('======================')
print(test)

# =================================================
# Answer 2: Using OS.walk()

test1 = output_dir_contents("C:\\Users\\jongguk\\PycharmProjects\\Python-for-Trading\\example scripting")














# =================================================














