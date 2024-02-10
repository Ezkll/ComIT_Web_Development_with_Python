# 20) Write a Python program that declares an integer variable B and assign it a value. It then displays a message indicating whether the value of B is positive or negative. We will consider 0 as positive.

B = int(input("Enter a Number :"))

if B >= 0:
    print(f"{B} is Positive")
else:
    print(f"{B} is Negative")