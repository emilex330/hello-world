num1 = 0
num2 = 0

num1 = int(input("Enter a row num from 1 to 5: "))
num2 = int(input("Enter a row num from 1 to 5: "))

# I used this website to get help for this exercise
# https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/ 
rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]
 
arr[num1 - 1][num2 - 1] = 1
for i in arr:
    print(i)