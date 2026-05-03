secret_number = 4
guess = None
while guess != secret_number:
 guess = int(input("Enter Your Secret Number eg.(1-10): "))
 if guess != secret_number:
     print("Wrong, Try Again!")
 else:
     print("Right, You found it!")