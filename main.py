print("welcome")
correct_password = "vancy@2026"
trial_attempt = 0
while trial_attempt < 3:
 trial = input('Please Enter Your Password: ')
 if trial == correct_password:
     print("Password is correct!")
     break
 else:
     print("Wrong, Please Try Again")
     trial_attempt += 1
 if trial_attempt == 3:
     print("Account Locked")





