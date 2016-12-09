'''
# origin code
=========================
input_id = input("아이디를 입력해주세요.\n")
members = ['egoing', 'k8805', 'leezche']
for member in members:
    if member == input_id:
        print('Hello!, '+member)
        import sys
        sys.exit()
print('Who are you?')
=========================
# end of origin code
'''
#  함수를 사용하여 로그인 코딩하기
input_id = input("아이디를 입력해주세요.\n")

def login(_id):
    members = ['egoing', 'k8805', 'leezche']
    for member in members:
        if member == _id:
            return True
        else:
            return False
if login(input_id):
    print('Hello!, '+input_id)
else:
    print('Who are you?')