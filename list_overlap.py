a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# c is where the similar values will  be added
c = []
for item in a:
    if item in b:
        c.append(item)

#the piece below creates a dictionary and removes the duplicate values 
c = list(dict.fromkeys(c))

print(c)