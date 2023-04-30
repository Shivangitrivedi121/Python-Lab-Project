import random
import time as t
def action(choice):
    sum_h=sum_b=0
    print("okay!go for it!")
    t.sleep(1)
    for die in range(0,choice):
        human=random.randint(1,6)
        print(f'''
             _______
            |       | 
            |{human} 
            |_______|   ''')

        t.sleep(1)
        print("you got:",human)
        sum_h+=human
    t.sleep(1)
    print("\nYOUR TOTAL IS:",sum_h)
    t.sleep(1)
    print("\n Now its my turn")
    t.sleep(1)
    for die in range(0,choice):
        bot=random.randint(1,6)
        print(f'''
              ________
             |        |
             | {bot} 
             |________|   ''')
      
        t.sleep(1)
        print("I got:",bot)
        sum_b+=bot 
    t.sleep(1)
    print("\n MY TOTAL IS:",sum_b)
    t.sleep(2)
    result="YOU WIN"if sum_h>sum_b else "\nI win"if sum_h<sum_b else "IT A TIE"
    print (result)   
    t.sleep(1)
def play():
    die=0
    roll="yes"
    while die==0:
        choice=int(input("how many dice do you want to throw?(1-6)"))
        if choice>0 and choice<6:
            action(choice)
            break
        else:
            print("please enter a valid choice")
    print("do you want to continue?(yes/no)")
    while roll== "yes":
        roll=input().lower().capitalize()
        if roll!="yes":
           play()
        else:
           print("It was nice playing with you! baye!")
           break
 
play()