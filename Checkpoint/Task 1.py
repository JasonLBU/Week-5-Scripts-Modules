#  Task 1
def Username():
    Username = input("Greetings! How should we call you? ")
    if ("Lady" in Username or "Lord" in Username):
        print("It shall be so ", Username)
    else:
        print("You may not be known by that name!")
Username()

