from time import time

Password = input("Please enter your password: ")
Start_time = time()
Letters = "abcdefghijklmnopqrstuvwxyz"
Uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Numbers = "0123456789"
Special_characters = "!@#$%^&*()_+-=~`"
Combination = Letters + Numbers + Special_characters

Guess = []
for val in range (12):
    a = [i for i in Combination]
    for y in range (val):
        a = [x + i for i in Combination for x in a]
    Guess = Guess + a
    if Password in Guess:        
        break
    
print (f"{Password} : {len(Guess)} Guesses")
print (f"Runtime: {str(time() - Start_time)}")    