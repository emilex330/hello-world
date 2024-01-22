word = " "
letters = []

word = input("Enter a string: ")

for i in word:
    letters.append(i)

size = 3
elem = 0
elements = []

# I used this website for help
# https://www.altcademy.com/blog/how-to-split-a-list-in-python/#method-2-using-a-for-loop 
for i in range(0, len(letters), size):
        elem = letters[i:i + size]
        elements.append(elem)

print(elements)