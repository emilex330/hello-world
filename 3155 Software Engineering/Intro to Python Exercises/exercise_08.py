num = 10
inp = 0
i = 1
originalList = []
appearOnce = []

while i <= num:
    inp = int(input("Enter number " + str(i) + ": "))
    originalList.append(inp)
    i += 1

print("Original List: ", originalList)

for x in originalList:     
    y = originalList.count(x)
    if y == 1:
        appearOnce.append(x)

print("Nums that appear once: ", appearOnce)