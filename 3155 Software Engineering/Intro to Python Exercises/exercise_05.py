i = 0
j = 0
k = 0
num2 = 0
num3 = 0
list1 = []
list2 = []
list3 = []

while i < 5:
    num2 = int(input("Enter a number for the first list: "))
    list1.append(num2)
    i += 1

while j < 5:
    num3 = int(input("Enter a number for the second list: "))
    list2.append(num3)
    j += 1 

print("First List: ", list1)
print("Second List: ", list2)

while k < 5:
    if list1[k] in list2 and list1[k] not in list3:
        list3.append(list1[k])
    if list2[k] in list1 and list2[k] not in list3:
        list3.append(list2[k])
    k += 1
print("Common List: ", list3)
