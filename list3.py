# List pratice set (1-2)
#Q1.sum & Average of List. Create a list of  numbers, then calculate and print the total sum and average.
a=[23,45,65,77,88]
sum = 0
for i in a:
    sum=sum+i
print(f"The total sum list of number  is  {sum}")
print(f"Average of your list numbers are {sum/len(a)}")

#Q2.Maximum Element with index.Find the largest element in the list along with its position(index)
a = [23,45,65,77,88,90]
max = a[0]
index = 0

for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        index = i

print(f"Your maximum element is {max} at index {index}")

#Q3.Second Greatest Element. identify the second-largest element in the list without sorting directly.
a = [23,45,65,77,88,90]

max = a[0]
max2 = a[0]
index = 0
index2 = 0

for i in range(len(a)):
    if a[i] > max:
        max2 = max
        max = a[i]
        index2 = index
        index = i
    elif a[i] > max2:
        max2 = a[i]
        index2 = i
print(f"maximum {max} at index No:- {index} and 2nd maximum is {max2} at 2nd index No:- {index2}")

#Q4. Check if List sorted(Increasing) Verify whether the list elements are in ascending order.
a = [23,45,65,77,88,90]
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        continue
    else:
        print("Your list is not sorted")
        break
else:
    print("Your list is sorted")

#Q5.Left Rotation by 1.Shift all elements one position to the left, with the first element moving to the end.
a = [10,20,30,40,50]

for i in range(len(a)-1):
    a[i],a[i+1] = a[i+1],a[i]

print("Left Rotation :- ",a)

#Q6.Right Rotation
a = [10,20,30,40,50]

for i in range(len(a)-1,0,-1):
    a[i],a[i-1] = a[i-1],a[i]

print("Right Rotation :- ",a)

#Q7.Reverse List(in place) Reverse the entire list without using extra space(i.e.,swap elements)
a = [10,20,30,40,50]
b = len(a)-1

for i in range(len(a)//2):
    a[i],a[b] = a[b],a[i]
    b = b-1
print(a)

#Q8.Linear search.search for a given element by checking each element one by one
a = [23,45,7,87,43,23,90,45,55]
search = 90

for i in range(len(a)):
    if a[i]  == search:
        print(f"element found at {i}")
        break
else:
    print("Sorry no such element exist")

#Q9.Binary Search. Efficiently search for an element in a sorted list using the divide-and-conquer approch.
a = [10,12,24,44,89,90,97,99,100]
search = 44
last = len(a)-1
start = 0
mid = (start + last)//2

while start <= last:
    if a[mid] == search:
        print(f"element found at index {mid}")
        break
    elif a[mid] < search:
        start = mid + 1
        mid = (start + last)//2

    elif a[mid] > search:
        last = mid -1
        mid = (start + last)//2
else:
    print("Sorry no such element exist")

#Q10.Bubbel Sort.sort the list by repatedly swapping adjacent elements if they are in the worng.
a = [45,50,6545,34,89,76,32,90,12,987]
for j in range(len(a)-1):
    for i in range(len(a)-1-j):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
print("your buble sort of number:- ",a) 

#Q11.Selection Sort.sort the list by selecting the smallest element in each pass and placing it in the correct position.
a = [45,50,6545,34,89,76,32,90,12,987]

for i in range(len(a)):
    j = i+1
    min = i
    for k in range(j,len(a)):
        if a[k] < a[min]:
            min = k
    a[i],a[min] = a[min],a[i]
print(f"your selection sort of number:- {a}")



