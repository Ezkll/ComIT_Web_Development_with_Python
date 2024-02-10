# 16) Write a program in Python that reads an integer from the keyboard and makes the sum of the next 100 numbers, showing the result on screen.

number = int(input("Enter a Number : "))
total = sum(range(number+1, number+101))
print(total)
total = 0

for number in range(number+1, number+101):
 print(number)
 total = total + number

print(total)