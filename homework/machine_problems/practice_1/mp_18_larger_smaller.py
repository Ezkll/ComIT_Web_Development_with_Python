# 18) Write a program in Python that reads two numbers on the keyboard and say which is the largest and which is the smallest.

num_1 = input("Enter first Number: ")
num_2 = input("Enter second Number: ")
if num_1 > num_2:
    print(f"The First Number: {num_1} is greater than the Second Number: {num_2}")
elif num_2 > num_1:
    print(f"The Second Number: {num_2} is greater than the First Number: {num_1}") 
else:
    print(f"The First Number: {num_1} is equal to the Second Number: {num_2}") 