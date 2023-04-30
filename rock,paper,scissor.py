import random
a=input("START THE GAME \n *press enter*\nand choose the number")
ls=["rock","scissor","paper"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
 game start .... 
 1 Yes
 2 No | Exit 
       '''))  
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1 rock
2 scissor
3 paper 
'''))   
            if userInput==1:
               uchoice="rock"
            elif userInput==2:
               uchoice="scissor"
            elif userInput==3:
               uchoice="paper"
            Cchoice=random.choice(ls)
            if Cchoice==uchoice:
               print("computer Value",Cchoice)
               print("user Value",uchoice)
               print("game Draw")
               ucount=ucount+1
               ccount=ccount+1
            elif(uchoice=="rock" and Cchoice=="scissor") or(uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
               print("computer Value",Cchoice)
               print("user Value",uchoice)
               print("You Win") 
               ucount=ucount+1
            else:
               print("computer Value",Cchoice)
               print("user Value",uchoice)
               print("computer Win")
               ccount=ccount+1

        if ucount==ccount:
           print("Final Game Draw...")
           print("User Score",ucount)
           print("computer score",ccount)
        elif ucount>ccount:
           print("Final you Win the Game...")
           print("User Score",ucount)
           print("computer score",ccount)
        else:
           print("Computer Win The Game ...")
           print ( "User Score",ucount)
           print("computer score",ccount)   

                    
    else:
       break        

                                                   