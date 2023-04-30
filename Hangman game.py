import random as r
print("-------------GUESS THE WORD-------------".center(40))
c=r.choice(['operating','computer','moniter','machine'])
m=r.randint(1,len(c))
n=r.randint(1,len(c))
l=[]
e=0
for i in range(len(c)):
    if i==n:
        l.append(c[i])
        print(c[i],end=' ')
    elif i==m:
        print(c[i],end=' ')
        l.append(c[i])
    else:
        print('_',end=' ')
        l.append('_')

while(1):
    a=input("\nEnter the missing word")
    if a in c:
        s=''
        b=c.index(a)
        l[b]=c[b]
        print("You Guessed Right")
        for i in l:
            s=s+i
        print(s)
        if s==c:
            print("You Guessed the Word")
            break
    else:
        print("Wrong Word")
        e=e+1
        if e==0:
            print('''
                 +------+ 
                 O      |
                        |
                        |
                        |
                    +=======+''')
        elif e==1:
            print('''
                 +------+ 
                 O      |
                 |      |
                        |
                        |
                    +=======+''')
        elif e==2:
            print('''
                 +------+ 
                 O      |
                /|      |
                        |
                        |
                    +=======+''')
        elif e==3:
            print('''
                 +------+ 
                 O      |
                /|\     |
                        |
                        |
                    +=======+''')
        elif e==4:
            print('''
                 +------+ 
                 O      |
                /|\     |
                /       |
                        |
                    +=======+ ''')
        elif e==5:
            print('''
                 +------+ 
                 O      |
                /|\     |
                / \     |
                        |
                    +=======+''')
            print("You Failed\nCorrect Word :",c)
            break