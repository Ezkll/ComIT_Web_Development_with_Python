# 19) Write a Python program that does the following: declare a variable N of type int, a variable A of type double and a variable C of type char and assign to each one a value. The following screen displays:
# The value of each variable. The sum of N + A. And A - N

N = 7
A =6.9
C = 'X'

print(f"N = {N}")
print(f"A = {A:.2f}")
print(f"C = {C}")

sum = N + A
print(f"The Sum of N and A = {sum:.2f}")
difference = A - N
print(f"The Diffence of A and N = {difference:.2f}")
