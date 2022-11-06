# Task 3
def Password():
    valid = True
    while (valid):
        Password = input("Greetings! What is the password? ")
        if Password == "parrot":
            print("Correct! You may enter.")
            valid = False
        else:
            print("Incorrect! You may try again.")
Password()