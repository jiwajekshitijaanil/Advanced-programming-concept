n = int(input("Enter a positive integer n: "))
i#f n > 0:
 total = 0
 i = 1
    while i <= n:
        total += i
        i += 1
    print("Sum of natural numbers up to", n, "is:", total)
else:
    print("Please enter a positive integer.")