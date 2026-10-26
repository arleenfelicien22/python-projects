import random
secret = random.randint(1,100)
attempts=0
while attempts < 7:
    guess = int(input("Guess a number:"))
    attempts=attempts+1
    if(guess == secret):
        print("bravo you found the secret:", secret, "in attempt", attempts)
        break
    elif(guess < secret):
        print("Too Low")
    elif(guess> secret):
        print("Too  High")
if(guess != secret):
    print("you Lost, the secret was", secret)