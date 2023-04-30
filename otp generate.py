import random
p=int(input('entre 1 for generating 4 digit otp and 2 for 6 digit otp: ',))
if(p==1):
    otp=''
    for i in range(4):
        s=str(random.randint(0,9))
        otp=otp+s
    print('Your four digit OTP is',otp)
if(p==2):
    otp=''
    for i in range(6):
        s=str(random.randint(0,9))
        otp=otp+s
    print('Your six digit OTP is',otp)