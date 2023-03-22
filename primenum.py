# Program to check if a number is prime or not

num = int(input("Enter a number :"))
if num < 1:
    print("is not a prime number")

else:
    for a in range(2, num):
        if (num % a) == 0:
            print("is not a prime number")
            break

    else:
        print("is a prime number")
