import random
import string
code = string.ascii_letters + string.digits + string.punctuation
def generate_password(length):
    shuffled = random.sample(code, len(code))
    password = ''.join(random.choices(shuffled, k=length))
    return password
length = int(input("Enter the desired length of your password (8 or more recommended): "))
password = generate_password(length)
print("Your secure password is:", password)
