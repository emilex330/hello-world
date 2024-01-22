num1 = 0
num2 = 0.0
i = 1
myList = []
num = int(input("Enter a number: "))

while i <= num:
    num2 = float(input("Enter number " + str(i) + ": "))
    myList.append(num2)
    i += 1

print("List: ", myList)
listLength = len(myList)

i = 0
total = 0.0
while i < listLength:
    total += myList[i]
    i += 1

print("Average: ", total / listLength)