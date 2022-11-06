# Task 2
def CafeMenu():
    Spam = int(input("How many slices of spam? "))
    print("Egg with", "".join('spam, ' * Spam) + "coming up!")
CafeMenu()