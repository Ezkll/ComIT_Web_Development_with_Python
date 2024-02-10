## Unit 3
### Practice III : Algorithms
---
### Goal of the practice

Become familiar with the writing of algorithms in pseudo code and the logic required to program. Handle the agreed
nomenclature.
Management of the basic data types and their correct application.
Using advanced flow control cycles and actions.
Understanding expressions and properly apply the precedence of operators.

1) What are the differences and similarities between an identifier and a reserved word.

    **``Identifiers``** are names given to entities like variables, functions, classes, etc. They are user-defined and can be almost any combination of letters and digits, as long as they follow these rules:

    - Identifiers cannot be a keyword.
    - Identifiers are case-sensitive.
    - They must start with a letter or an underscore (_), but not a digit.
    - They cannot contain whitespace or special symbols like !, @, #, $, etc.

    **``Reserved``** words, on the other hand, are predefined words that have special meanings to the Python interpreter. They are used to define the syntax and structure of the Python language. Here are some rules about reserved words:

    - Reserved words cannot be used as identifiers.
    - All reserved words in Python should be in lowercase, except for True, False, and None.

    The **``similarities``** between identifiers and reserved words are that they are both integral parts of Python syntax and are used to make the code meaningful.

    The **``differences``** between identifiers and reserved words lie in their usage and rules. ***``Identifiers are user-defined``***** and can be named freely within the rules, while ***``reserved words are predefined``*** and cannot be used as identifiers.

2) Create an algorithm to determine the largest of 3 numbers.

        algorithm findLargestNumber ()
        var Number: num1, num2, num3, largest
        read(num1)
        read(num2)
        read(num3)
        if num1 > num2 and num1 > num3 then
            largest = num1
        else if num2 > num1 and num2 > num3 then
            largest = num2
        else
            largest = num3
        end if
        print("The largest number is " + largest)
        end algorithm


3) Create an algorithm to determine the largest of a series of numbers that are read from the keyboard. The user
ends by entering -1.

        algorithm findLargestNumber ()
        var Number: num, largest
        print("Enter a number (-1 to end): ")
        read(num)
        largest = num
        while num != -1 do
            if num > largest then
                largest = num
            end if
            print("Enter a number (-1 to end): ")
            read(num)
        end while
        print("The largest number is " + largest)
        end algorithm


4) Write an algorithm to determine the least of a series of numbers that are read from the keyboard. The user ends by entering -1. What differences do you find with respect to the previous algorithm?

        algorithm findSmallestNumber ()
        var Number: num, smallest
        print("Enter a number (-1 to end): ")
        read(num)
        smallest = num
        while num != -1 do
            if num < smallest then
                smallest = num
            end if
            print("Enter a number (-1 to end): ")
            read(num)
        end while
        print("The smallest number is " + smallest)
        end algorithm

    The main difference between this algorithm and the previous one is the comparison operator used in the if statement inside the loop. In the previous algorithm, we used the ``>`` operator to find the largest number, whereas in this algorithm, we use the ``<`` operator to find the smallest number. 

5) Write an algorithm to print and count the multiples of 3 from 1 to a number that we enter by keyboard.

        algorithm printAndCountMultiplesOfThree ()
        var Number: num, i, count
        count = 0
        print("Enter a number: ")
        read(num)
        for i = 1 to num do
            if i mod 3 == 0 then
                print(i)
                count = count + 1
            end if
        end for
        print("The number of multiples of 3 is " + count)
        end algorithm

6) Write an algorithm that reads a series of real numbers and adds them, printing the result. The series ends when the user enters the number zero.

        algorithm addRealNumbers ()
        var Real: num, sum
        sum = 0
        print("Enter a real number (0 to end): ")
        read(num)
        while num != 0 do
            sum = sum + num
            print("Enter a real number (0 to end): ")
            read(num)
        end while
        print("The sum of the real numbers is " + sum)
        end algorithm

7) Write an algorithm to find the average of a series of numbers that are read from the keyboard. Compare this exercise with the previous one. What are the differences and similarities?

        algorithm calculateAverage ()
        var Real: num, sum, count
        sum = 0
        count = 0
        print("Enter a number (0 to end): ")
        read(num)
        while num != 0 do
            sum = sum + num
            count = count + 1
            print("Enter a number (0 to end): ")
            read(num)
        end while
        if count != 0 then
            print("The average of the numbers is " + sum / count)
        else
            print("No numbers were entered.")
        end if
        end algorithm

    **``Similarities``**

    - Both algorithms read a series of numbers from the user.
    - Both use a while loop to process the series of numbers.
    - Both print a result after the loop ends.

    **``Differences``**

    - The previous algorithm adds the numbers, while this one calculates their average.
    - This algorithm keeps track of the count of numbers entered, which is not needed in the previous algorithm.

8) Given a series of real numbers that are being read from the keyboard, determine the maximum value and the position of it.

        algorithm findMaxAndPosition ()
        var Number: max, num
        var Number: position, i = 1
        read(num)
        max = num
        position = i
        while (num != 0)
            i = i + 1
            read(num)
            if (num > max)
            max = num
            position = i
            end if
        end while
        print("The maximum value is " + max + " at position " + position)
        end algorithm

9) Write an algorithm that requests the reading of a series of individual characters and count how many times the letter "a" is entered. The user ends by entering the "$" symbol.

        algorithm countLetterA ()
        var Character: ch
        var Number: count = 0
        read(ch)
        while (ch != '$')
            if (ch == 'a' or ch == 'A')
            count = count + 1
            end if
            read(ch)
        end while
        print("The letter 'a' was entered " + count + " times.")
        end algorithm


10) Develop an algorithm to count the number of students whose weight is between 50 and 60, between 61 and 80 and between 81 and 100. The weights are entered by keyboard and report the number of students in each category of weight. How does the algorithm change if I want to accumulate weight totals for each category?

        algorithm countWeightCategories ()
        var Number: weight
        var Number: count50_60 = 0, count61_80 = 0, count81_100 = 0
        read(weight)
        while (weight != 0)
            if (weight >= 50 and weight <= 60)
            count50_60 = count50_60 + 1
            else if (weight >= 61 and weight <= 80)
            count61_80 = count61_80 + 1
            else if (weight >= 81 and weight <= 100)
            count81_100 = count81_100 + 1
            end if
            read(weight)
        end while
        print("Number of students in weight category 50-60: " + count50_60)
        print("Number of students in weight category 61-80: " + count61_80)
        print("Number of students in weight category 81-100: " + count81_100)
        end algorithm

    Accumulate weight totals for each category.

        algorithm countAndAccumulateWeightCategories ()
        var Number: weight
        var Number: count50_60 = 0, count61_80 = 0, count81_100 = 0
        var Number: total50_60 = 0, total61_80 = 0, total81_100 = 0
        read(weight)
        while (weight != 0)
            if (weight >= 50 and weight <= 60)
            count50_60 = count50_60 + 1
            total50_60 = total50_60 + weight
            else if (weight >= 61 and weight <= 80)
            count61_80 = count61_80 + 1
            total61_80 = total61_80 + weight
            else if (weight >= 81 and weight <= 100)
            count81_100 = count81_100 + 1
            total81_100 = total81_100 + weight
            end if
            read(weight)
        end while
        print("Number of students in weight category 50-60: " + count50_60 + ", Total weight: " + total50_60)
        print("Number of students in weight category 61-80: " + count61_80 + ", Total weight: " + total61_80)
        print("Number of students in weight category 81-100: " + count81_100 + ", Total weight: " + total81_100)
        end algorithm

11) Write an algorithm to determine if a number read by keyboard is prime.

        algorithm isPrime ()
        var Number: num, i
        var Boolean: prime = true
        read(num)
        if (num < 2)
            prime = false
        else
            for i = 2 to sqrt(num)
            if (num mod i == 0)
                prime = false
                break
            end if
            end for
        end if
        if (prime)
            print(num + " is a prime number.")
        else
            print(num + " is not a prime number.")
        end if
        end algorithm

12) Write an algorithm to print and count numbers that are multiples of 2 or 3 that are between 1 and 100.

        algorithm printAndCountMultiples ()
        var Number: i, count = 0
        for i = 1 to 100
            if (i mod 2 == 0 or i mod 3 == 0)
            print(i)
            count = count + 1
            end if
        end for
        print("There are " + count + " numbers between 1 and 100 that are multiples of 2 or 3.")
        end algorithm

13) Develop an algorithm to determine if a series of numbers that the user is entering is in increasing order or not.

        algorithm isIncreasing ()
        var Number: num, prevNum
        var Boolean: increasing = true
        read(num)
        prevNum = num
        read(num)
        while (num != 0)
            if (num < prevNum)
            increasing = false
            break
            end if
            prevNum = num
            read(num)
        end while
        if (increasing)
            print("The series is in increasing order.")
        else
            print("The series is not in increasing order.")
        end if
        end algorithm


