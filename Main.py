from time import time

Password = input("Please enter your password: ")
Start_time = time()
Letters = "abcdefghijklmnopqrstuvwxyz"
Numbers = "0123456789"
Special_characters = "!@#$%^&*()_+-=~`"
Combination = Letters + Numbers + Special_characters

Guess = []
for val in range (12):
    a = [1 for 1 in Combination]
    for y in range (val):
        a = [x + 1 for 1 in Combination for x in a]
    guess = guess + a
    if Password in Guess:        
        break
    
print (f"{Password} : {len(Guess)} Guesses")
print (f"Runtime: {str(time() - Start_time)}")    