inp = 0
list1 = []
list2 = []

while True:
    inp = input("Enter a number or QUIT to quit: ")

    if inp == "QUIT":
        break
    else:
        list1.append(int(inp))
        if int(inp) % 2 == 0:
            list2.append(int(inp))
print(list1)
print(list2)