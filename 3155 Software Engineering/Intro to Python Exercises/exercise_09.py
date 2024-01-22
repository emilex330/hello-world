words = []
word = " "
i = 0

while i <= 4:
    word = input("Enter a word: ")
    words.append(word)
    i += 1

print("Words: ", words)

# I used this website how to find out how to print a list in one line 
# https://www.scaler.com/topics/how-to-print-in-same-line-in-python/ 
print("One string: ", end = "")
for x in words:     
    print(x, end = " ")