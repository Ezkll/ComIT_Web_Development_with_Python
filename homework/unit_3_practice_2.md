## Unit 3
### Practice II : Algorithms
---
### Goal of the practice
Become familiar with the writing of algorithms in pseudo code, expressions, operands, operators, assignments, conditionals and the elementary logic required to program.

1) What is the difference between the contents of a variable and its name?

    > The variable name can be thought of as a drawer, and the drawer may contain anything which can be the content of the variable.

2) What is the difference between a variable, a constant and a literal? What do they have in common?

    ``Variable`` A variable is a named storage location that a programmer can use to store, retrieve or manipulate data. The value of a variable can change during the execution of a program.

    ``Constant`` A constant, like a variable, is also a named storage location, but its value is set at the time of initialization and cannot be changed afterwards. It’s used when you have a value that you want to remain the same throughout the program.

    ``Literal`` A literal is a value that is written exactly as it’s meant to be interpreted. In other words, it’s a constant value embedded directly into the code. For example, in the statement int x = 10;, 10 is an integer literal.

    What they have in common is that they all represent data values in a program. They are fundamental building blocks of programming and are used to make the code more flexible, readable, and maintainable. 

3) What is an expression?

    > It is a combination of one or more constants, variables, functions, and operators that the programming language interprets

4) What are the elements in an assignment?

5) Debug the following assignments, writing the value that the variable gets in each assignment.

    ``X <- 0``

        X will contain the value 0

    ``X <- X + 4``

        X will contain X + 4
        Since X has the current value 0
        X is now 4

    ``X <- X + X – X * X``

        Here, we’re performing several operations on X, which is currently 4. 
        X becomes 4 + 4 - 4 * 4 
        = 8 - 16 
        = -8

    ``X <- X mod 4``

        X modulo 4. 
        Since X is -8, X becomes -8 mod 4 = 0
        Since -8 is exactly divisible by 4

    ``X <- (x + 4) div 2``

        Add 4 to X (which is 0)
        Divide by 2 
        Assign the integer division result back to X
        So, X becomes (0 + 4) div 2 = 4 div 2 = 2.

    Final Value 
    ``X = 2``


6) Determine the operands (specifying which type of operand is), and operators (specifying their name) of the following expressions.

        Group with parentheses to clarify which operations are performed first.
        Assuming that x <- 10, y <- 10, n <- 4 and a <- 1
        Calculate the expressions and write the results.

    var Number: x, y, a, n

    const Number: PI = 3,1416

    const Number: COFACTOR = 1

            PI + x / 2
    
    ``Operands`` *constant* ``PI`` , *variable* ``x`` , *literal* ``2`` 
    
    ``Operators`` *addition* ``+`` and *division* ``/``

    ``Grouping`` ``(PI + (x / 2))``

    ``Calculation`` 

        PI + x / 2
        x = 10 
        PI = 3.1416: 
    
            = 3.1416 + 10 / 2
            = 3.1416 + 5
            = 8.1416
    
    ##### 
        y
    ``Operand`` *variable* ``y`` = ``10``
    
        x + y – a

    ``Operands`` *variables* ``x``, ``y``, ``a`` 

     ``Operators`` *addition* ``+`` and *subtraction* ``-``

    ``Grouping`` ``((x + y) - a)``
    
    ``Calculation`` 
            
        x + y – a
        x = 10
        y = 10
        a = 1
            
            10 + 10 - 1 = 19

    #####   
        n mod 2 == 0
    
    ``Operands`` *variable* ``n``, *literals* ``2``, ``0``
    
    ``Operators`` *modulo* ``mod``, *equality comparison* ``==``

    ``Calculation``
            
        n mod 2 == 0
        n = 4
        
            4 mod 2 == 0 
            true

    ``Grouping`` ``((n mod 2) == 0)``
   
        COFACTOR * x > 20

    ``Operands`` *constant* ``COFACTOR``, *variable* ``x``, *literal* ``20`` 

    ``Operators`` *multiplication* ``*``, *greater than comparison* `>`

    ``Grouping`` ``((COFACTOR * x) > 20)``

    ``Calculation``
    
        COFACTOR = 1
        x = 10

             1 * 10 > 20 
             false
    #####         
            COFACTOR

    ``Operand`` *constant* ``COFACTOR``

    ``Calculation``
            
        COFACTOR = 1
        
            1
    
7) Write an algorithm to read a number by keyboard and say if it is positive or negative.

        1. Start
        2. Display "Please enter a number:"
        3. Read the input number from the keyboard and store it in a variable, let's call it 'num'
        4. If 'num' is greater than 0 Then
        5.     Display "The number is positive."
        6. Else If 'num' is less than 0 Then
        7.     Display "The number is negative."
        8. Else
        9.     Display "The number is zero."
        10. End If
        11. End

8) Perform an algorithm to read a number and report if it is greater, equal or less than zero.

        1. Start
        2. Display "Please enter a number:"
        3. Read the input number from the keyboard and store it in a variable, let's call it 'num'
        4. If 'num' is greater than 0 Then
        5.     Display "The number is greater than zero."
        6. Else If 'num' is less than 0 Then
        7.     Display "The number is less than zero."
        8. Else
        9.     Display "The number is equal to zero."
        10. End If
        11. End

9) Write an algorithm that determines if a number is even.

        1. Start
        2. Display "Please enter a number:"
        3. Read the input number from the keyboard and store it in a variable, let's call it 'num'
        4. If 'num' mod 2 equals 0 Then
        5.     Display "The number is even."
        6. Else
        7.     Display "The number is odd."
        8. End If
        9. End

10) Make an algorithm to read two real numbers and print the largest of them.

        1. Start
        2. Display "Please enter the first number:"
        3. Read the first input number from the keyboard and store it in a variable, let's call it 'num1'
        4. Display "Please enter the second number:"
        5. Read the second input number from the keyboard and store it in a variable, let's call it 'num2'
        6. If 'num1' is greater than 'num2' Then
        7.     Display "The largest number is: " and 'num1'
        8. Else If 'num2' is greater than 'num1' Then
        9.     Display "The largest number is: " and 'num2'
        10. Else
        11.     Display "Both numbers are equal."
        12. End If
        13. End

11) Given the radius of a circle, make an algorithm to calculate the value of the area.

        1. Start
        2. Display "Please enter the radius of the circle:"
        3. Read the input radius from the keyboard and store it in a variable, let's call it 'r'
        4. Calculate the area of the circle using the formula: Area = PI * r^2
        5. Display "The area of the circle is: " and the calculated area
        6. End

12) Write an algorithm that determines if an "N" number is divisible by another "M".

        1. Start
        2. Display "Please enter the first number (N):"
        3. Read the input number from the keyboard and store it in a variable, let's call it 'N'
        4. Display "Please enter the second number (M):"
        5. Read the input number from the keyboard and store it in a variable, let's call it 'M'
        6. If 'N' mod 'M' equals 0 Then
        7.     Display "N is divisible by M."
        8. Else
        9.     Display "N is not divisible by M."
        10. End If
        11. End

13) Write an algorithm to translate a time expressed in days, hours, minutes and seconds to time expressed in seconds.

        1. Start
        2. Display "Please enter the number of days:"
        3. Read the input number of days from the keyboard and store it in a variable, let's call it 'days'
        4. Display "Please enter the number of hours:"
        5. Read the input number of hours from the keyboard and store it in a variable, let's call it 'hours'
        6. Display "Please enter the number of minutes:"
        7. Read the input number of minutes from the keyboard and store it in a variable, let's call it 'minutes'
        8. Display "Please enter the number of seconds:"
        9. Read the input number of seconds from the keyboard and store it in a variable, let's call it 'seconds'
        10. Calculate the total time in seconds using the formula: TotalSeconds = days*24*60*60 + hours*60*60 + minutes*60 + seconds
        11. Display "The total time in seconds is: " and the calculated TotalSeconds
        12. End

14) We are being informed of three environmental temperature values, and we are asked to develop an algorithm to calculate and report the sum and average of these values.

        1. Start
        2. Display "Please enter the first temperature value:"
        3. Read the first input temperature from the keyboard and store it in a variable, let's call it 'temp1'
        4. Display "Please enter the second temperature value:"
        5. Read the second input temperature from the keyboard and store it in a variable, let's call it 'temp2'
        6. Display "Please enter the third temperature value:"
        7. Read the third input temperature from the keyboard and store it in a variable, let's call it 'temp3'
        8. Calculate the sum of the temperatures: Sum = temp1 + temp2 + temp3
        9. Calculate the average of the temperatures: Average = Sum / 3
        10. Display "The sum of the temperatures is: " and the calculated Sum
        11. Display "The average of the temperatures is: " and the calculated Average
        12. End

15) For our brave ones: translate a time expressed in seconds to a time expressed in days, hours, minutes and seconds.

        1. Start
        2. Display "Please enter the time in seconds:"
        3. Read the input time from the keyboard and store it in a variable, let's call it 'totalSeconds'
        4. Calculate the number of days: days = totalSeconds div (24*60*60)
        5. Calculate the remaining seconds: remainingSeconds = totalSeconds mod (24*60*60)
        6. Calculate the number of hours: hours = remainingSeconds div (60*60)
        7. Update the remaining seconds: remainingSeconds = remainingSeconds mod (60*60)
        8. Calculate the number of minutes: minutes = remainingSeconds div 60
        9. Update the remaining seconds: seconds = remainingSeconds mod 60
        10. Display "The time in days, hours, minutes, and seconds is: " and the calculated days, hours, minutes, and seconds
        11. End
