# Python Conditional Statement (Partice Questions)

# 1. Write a Python program to check whether a number is positive, negative, or zero
num=int(input("Tell a number:- "))
if num > 1:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

#Q2.2. Write a program to check if a number is even or odd.
num=float(input("tell a number:- "))
if num%2 == 0:
    print("even number")
else:
    print("odd number")

#Q3. Check whether a person is eligible to vote (age >= 18)
age=float(input("Tell your age:- "))
if age >=18:
    print("eligible for vote")
else:
    print("not eligible for vote")

#Q4. Write a program to find the largest of two numbers
num1=float(input("Tell 1st number:- "))
num2=float(input("Tell 2nd number:- "))
if num1 >= num2:
    print("num1 is greater than num2")
else:
    print("num2 is greater than num1")

# 5. Write a program to find the largest among three numbers.
num1=float(input("Tell your 1s number:- "))
num2=float(input("Tell ypur 2nd number:- "))
num3=float(input("Tell your 3rd number:- "))
if num1 > num2 and num1 > num3:
    print("num1 is greater")
elif num2 > num1 and num2 >num3:
    print("num2 is greater")
elif num3 > num1 and num3 > num2:
    print("num3 is greater")
else:
    print("Invalid number! plzz check your digit or number")

#Q6. Check whether a given year is a leap year or not
year=float(input("Tell a year:- "))
if year%4 == 0:
    print("leap year")
else:
    print("Not leap year")

#Q7. Write a program to check whether a character is a vowel or consonant
ch=input("enter the character:- ")
if ch.isalpha():
    if ch in ('a','e','i','o','u','A','E','I','O','U'):
        print("It is a vowel")
    else:
        print("it is a consonant")
else:
    print("Invalid input! plese enter an alphabet.")

#Q8.Write a program to check if a number is divisible by 5 and 11 or not.
num=int(input("Tell your number:- "))
if num%5 == 0 and num%11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not Divisible by 5 and 11")

#9. Check whether a given number is a multiple of 3 or 7
num=int(input("Tell your number:- "))
if num%3 == 0 and num%7 == 0:
    print("Divisible by 3 and 7")
else:
    print("Not Divisible by 3 and 7")

#10. Write a program to classify a grade based on marks (A, B, C, D, Fail).
grade=int(input("Tell your number:- "))
if grade >= 80:
    print("Grade A")
elif grade >= 65:
    print("Grade B")
elif grade >= 50:
    print("Grade C")
elif grade >= 40:
    print("Grade D")
else:
    print("Fail")

#Q11. Write a program to check whether a number is within a given range (1 to 100)
num=int(input("Tell your number:-"))
if num >=1 and num<=100:
    print("The number is within the range(1 to 100)")
else:
    print("The number is OUT of the range!")

#Q12. Write a program to find whether a character is uppercase or lowercase.
ch=input("Tell your number:-")
if ch.isalpha():
    if ch.isupper():
        print("The character is Uppercase.")
    else:
        print("The character is Lowercase.")
else:
    print("Invalid input! Please enter a letter.")

#Q13. Write a program to check whether a given string is empty or not.
text=input("Tell your charchter:-")
if text == "":
    print("The string is Empty")
else:
    print("The string is NOT Empty")

#Q14. Check if a person is eligible for a senior citizen discount (age >= 60)
person=int(input("Tell your age:-"))
if  person >= 60:
    print("A person is eligible for a senior citizen discount")
else:
    print("A person is not eligible for a senior citizen discount ")

#Q15. Write a program to determine if a number is positive and even.
num=int(input("Tell your number:- "))
if num > 0 and num%2 == 0:
    print("Number is positive and even")
else:
    print(" Not Number is positive and even")

#Q16.Write a program to check whether a triangle is valid based on its angles.
a=float(input("Tell angle 1:-"))
b=float(input("Tell angle 2:- "))
c=float(input("Tell angle 3:- "))

if a > 0 and b > 0 and c > 0 and (a + b + c == 180):
    print("Triangle is valid")
else:
    print("Triangle is Not valid")

#Q17.Write a program to check whether a triangle is equilateral, isosceles, or scalene.

#Q18. Write a program to find the largest number among four numbers.
a = int(input("Enter the 1st number:- "))
b = int(input("Enter the 2nd number:- "))
c = int(input("Enter the 3rd number:- "))
d= int(input("Enter the 4th number:- "))

if a > b and a > c and a > d:
    print("A is largest")
elif b > a and b > c and b > d:
    print("B is Largest")
elif c > a and c > b and c > d:
    print("C is Largest")
else:
    print("D is Largest")

#Q19. Check whether a student has passed or failed based on marks (>= 40 pass)
hindi = int(input("Enter Hindi marks:- "))
eng = int(input("Enter English marks:- "))
math = int(input("Enter Math marks:- "))
comp = int(input("Enter Computer marks:-")) 
science = int(input("Enter Science marks:- "))

total=hindi+eng+math+comp+science
marks=500
per=(total/marks)*100

print(f"\n Total marks obtined:- {total}")
print(f"Precentage:-{per:.2f}%")

# 20. Write a program to check whether a number is a single-digit, double-digit, or more
num = int(input("Enter the number:- "))
if -9 <= num <= 9:
    print("The number is single digit number")
elif -99 <= num <= 99:
    print("The number is Double digit number")
else:
    print("The number has more than two digits")
# 21. Write a program to check whether a number is a perfect square
import math
num=int(input("Enter a number:- "))
if num < 0:
    print("Negative number can not be perfect number")
else:
    root = int(math.sqrt(num))
    if root * root == num:
        print(f"{num} is a perfect Square")
    else:
        print(f"{num} is Not perfect Square")
#Q22.Write a program to check if a person can drive (age >= 18 and has license)
age=int(input("Enter the Age:- "))
if age >= 18:
    print("Person can drive")
else:
    print("Person can not drive")

#Q23.Write a program to determine if a year is a century year (ends with 00).
year=int(input("Enter the Year:- "))
if year % 100 == 0:
    print("Century Year")
else:
    print("Not Century Year")

#24.Write a program to check if a number is positive and divisible by 3
num=int(input("Enter a number:- "))

if num > 0 and num % 3 == 0:
    print(f"{num} is positive and Divisible by 3")
elif num > 0:
    print(f"{num} is Positive but not Divisible by 3")
else:
    print(f"{num} is NOT a positive number")

#Q25. Write a program to check if a person can donate blood (age >= 18 and weight > 50)
age=int(input("Enter a age:- "))
weight=float(input("enter weight (in kg):-"))
if age >= 18 and weight > 50:
    print("A person can denoted blood")
else:
    print("A person can not denoted blood")

#Q26. Write a program to print 'Weekend' if the day is Saturday or Sunday, else 'Weekday'
day=input("Enter the day:-").strip().lower()
if day == "saturday" and day == "sunday":
    print("Weekend")
else:
    print("Weekday")

#Q 27. Write a program to check if a password length is strong (>= 8 characters).
password=input("Enter your password:- ")
if len(password) >= 8:
    print("Password is strong (length is sufficient)")
else:
    print("Password is weak(too short)")

#Q28. Write a program to check whether a temperature is hot, warm, or cold.
temp=int(input("Enter the temprature in c:- "))
if temp >= 30:
    print("Hot")
elif 15 <= temp < 30:
    print("Warm")
else:
    print("Cold")

#Q29.Write a program to check if a shop is open (between 9 AM to 9 PM).
time=int(input("Enter the time:- "))
if 9 <= time < 21:
    print("The shop is open")
else:
    print("The shop is closed!")

#Q30. Write a program to determine if a person is eligible for a loan (age >= 21, salary > 25000)
age=int(input("enter the age :- "))
salary=int(input("Enter the salary:- "))

if age >=18 and salary >= 25000:
    print("You can apply the loan")
else:
    print("You can not apply tha  loan")
 