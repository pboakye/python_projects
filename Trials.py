print('Welcome To The Password Length Checker!')
password = input("Please enter your password: ")
is_invalid=True
while is_invalid:
 if len(password) ==8:
    print("Password is accepted!!")
 elif len (password) <=7:
    print("Sorry, Password Cannot be less than 8")
 elif len(password) >8:
    print('Sorry, Password Cannot be more than 8')






