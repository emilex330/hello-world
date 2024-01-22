num = int(input("Enter an integer greater than 1: "))

for num in range(0, num + 1):
    print("The cube of ", num ," is: ", num * num * num)
    num -= 1
