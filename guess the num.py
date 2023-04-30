import random
n=random.randint(1,100)
att=3
a=input("____WELCOME TO THE GUESS GAME____")
while att:
    guess = int(input("Guess a number: "))
    if guess == n:
      print("Congratulations! You guessed the number correct",n)
      
    elif guess<n:
      print("The number is higher. Try again.")
    else:
      print("The number is lower. Try again.")   
    att-=1
print("sorry,the number was",n)    

