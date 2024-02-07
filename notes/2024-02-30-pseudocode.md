Algorithm to sum first N Numbers that are divisible by 3 with first
N Numbers divisible by 5.

        If N = 1 = 3 + 5
        If N = 2 = (3 + 6) + (5 + 10)
        If N = 5 = (3 + 6 + 9 + 12 + 15) + (5 + 10 + 15 + 20 + 25)

---

>total = total + (3 * counter) + (5 * counter)

    def sum_of_numbers(N):
        total = 0
        for counter in range(1, N + 1):
            total += (3 * counter) + (5 * counter)
        return total

    print(sum_of_numbers(1))  # Output: 8
    print(sum_of_numbers(2))  # Output: 24
    print(sum_of_numbers(5))  # Output: 120

---
Another solution:

        Algorithm DivisibleByFive(N):
            Initialize, divisible_by_5
            For i from 1 to N*5:
                If i is divisible by 5:
                    Add i to divisible_by_5
            EndFor
            Return divisible_by_5
        EndAlgorithm

        Algorithm DivisibleByThree(N):
            Initialize, divisible_by_3
            For i from 1 to N*3:
                If i is divisible by 3:
                    Add i to divisible_by_3
            EndFor
            Return divisible_by_3
        EndAlgorithm



Simplified:

        Algorithm SumOfNumbers(N):
            Initialize total to 0
            For i from 1 to N*3:
                If i is divisible by 3:
                    Add i to total
            EndFor
            For i from 1 to N*5:
                If i is divisible by 5:
                    Add i to total
            EndFor
            Return total
        EndAlgorithm