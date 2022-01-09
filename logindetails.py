class Login:
    def userdetail(self, email , password):
        self.__email = email
        self.__password = password
        return self.__email and self.__password
        
    def set_email(self, email):
        self.__email = email
        
    def get_email(self):
        return self.__email
    
    def set_password(self, password):
        self.__password = password
        
    def get_password(self):
        return self.__password

login = Login()

with open('D:\\Monster Project\\email.txt', 'r') as myfile:
    email_file = myfile.readline()
login.set_email(email_file)
with open('D:\\Monster Project\\password.txt', 'r') as myfile:
    password_file = myfile.readline()
login.set_password(password_file)

if __name__ == "__main__":
    print(login.get_email())
    print(login.get_password())
        