# Task 4
def password_checker(password):
    from string import ascii_letters as letters, digits, punctuation
    has_letter = has_digit = has_punc = False
    for character in password:
        if character in letters:
            has_letter = True
        elif character in digits:
            has_digit = True
        elif character in punctuation:
            has_punc = True
    return has_letter and has_digit and has_punc

Password = input("Please enter a password: ")
if (password_checker(Password)):
    print("The password fits all the critera and is acceptable")
else:
    print("The password doesn't fit all the critera and is not acceptable")