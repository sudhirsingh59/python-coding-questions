# For Loop Questions (Using Loops Only)
#Q1. Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

#Q2. Print even numbers between 1 and 50 using a for loop.
for i in range(1,51):
    if i%2 == 0:
        print(f"your even number is :-{i}")

#Q3. Print odd numbers between 1 and 50 using a for loop.
for i in range(1,51):
    if i%3 == 0:
        print("The odd number between 1 to 50 is:-",i)

#Q4. Print the multiplication table of any number given by the user.
num=int(input("Enter the number you want to table:- "))
for i in range(1,11):
    print(num, "x", i, "=", num * i)

#Q5. Print the sum of numbers from 1 to n using a loop.
num=int(input("enter the number you wan to sum:- "))
sum = 0
for i in range(1,num+1):
    sum += i
    print(f"sum from 1 to", num, "is:-",sum)

#Q6. Count how many digits are in a number using a loop
