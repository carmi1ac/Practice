a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

a = [item for item in a if item % 2 == 0]

print(a)


#uses the random library to generate a list and provides the even numbers from that list
import random

numlist = []
list_length = random.randint(5,15)


while len(numlist) < list_length:
    numlist.append(random.randint(1,75))

evenlist = [number for number in numlist if number % 2 == 0]

print(numlist)
print(evenlist)