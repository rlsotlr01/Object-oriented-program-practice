class User:
    history = ''
    def __init__(self):
        print('회원가입을 해주세요')
        self.userid = input('아이디를 입력해주세요.')
        User.history = User.history + '이용자의 아이디 : '+self.userid + '\n'


        while True:
            self.userpw = input('비밀번호를 입력해주세요. (8자 이상 16자 이하)')
            if len(self.userpw)>=8 and len(self.userpw)<=16:
                User.history = User.history + '이용자의 비밀번호 : ' + self.userpw + '\n'
                break
            else :
                continue

    def check_signin(self):
        print('당신의 아이디는 '+self.userid+'입니다')
        print('당신의 비밀번호는 '+self.userpw+'입니다')
        print('로그인 되었습니다.')

    def login(self,inserted_id,inserted_pw):
        while True:
            if self.userid==inserted_id and self.userpw==inserted_pw:
                print('로그인이 성공적으로 이루어졌습니다.')
                break
            else :
                print('아이디 또는 비밀번호가 틀렸습니다.')
                continue

    @classmethod
    def id_data(cls):
        print(User.history)

#sign-in 회원가입.
customer1 = User()
customer1.check_signin()
customer2 = User()
customer2.check_signin()

print('로그인을 해주세요.')
inserted_id = input('아이디는?')
inserted_pw = input('비밀번호는?')
customer1.login(inserted_id,inserted_pw)

User.id_data()
