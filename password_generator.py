import string
import random

def passw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

y = passw_gen(int(35))


char = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

passlen = input("Enter how many characters for your password: ")

x = "".join(random.sample(char, int(passlen) ))


z = ''.join(random.sample(x+y, int(passlen)))

print("Your new password: " + "\n" + z + "\n")