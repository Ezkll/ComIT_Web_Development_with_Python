On modularization and variables scope.
1. write an algorithm that invokes another one, and the invoked one prints a value.

        algorithm mainAlgorithm ()
        var Number: value
        value = 10
        invokePrintValue(value)
        end algorithm

        algorithm invokePrintValue (Number: value)
        print(value)
        end algorithm


2. write an algorithm that invokes another one to be called "add”, that receives two numbers. The "add" algorithm must add the parameters. The invoking algorithm should receive back that value and show it on screen.

        algorithm mainAlgorithm ()
        var Number: num1, num2, sum
        num1 = 10
        num2 = 20
        sum = add(num1, num2)
        print(sum)
        end algorithm

        algorithm add (Number: a, Number: b) -> Number
        var Number: result
        result = a + b
        return result
        end algorithm


3. write an algorithm and subalgorithm. Write two variables with the same name so that the compiler does not show an error.

        algorithm mainAlgorithm ()
        var Number: x
        x = 10
        subAlgorithm()
        print(x)
        end algorithm

        algorithm subAlgorithm ()
        var Number: x
        x = 20
        print(x)
        end algorithm


