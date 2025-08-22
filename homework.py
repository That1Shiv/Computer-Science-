import math

#question 1 
x = 300
y = 330

if y > x:
  print('y is greater than x')
else:
  print('y is not greater than x')

# #question 2
name = input('what is your name? ')
age = input('What is your age? ')
height = input('what is your height? ')
weight = input('what is your weight? ')

print("Your details are:")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Weight:", weight)

# #question 3 

food = input('What is your favourite food?  ')
name = input('What is your name? ')

print(name + ' likes ' + food)


# # question 4 

name = input('what is your name? ')
age = input('what is your age? ')
school = input('What school do you go to? ')

print(name + ' is ' + age + ' and goes to ' + school + ' school ')

#question 5 (reverse order)
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print(last_name + ' ' + first_name)

# question 6 
n = input("Enter an integer: ")
result = int(n) + int(n*2) + int(n*3)
print("Result:", result)

# question 7
radius = 6
volume = (4/3) * math.pi * radius**3
print("The volume of the sphere is:", volume)

# question 8 
number = int(input("Enter a number: "))
if number % 2 == 0:
  print("The number is even.")
else:
  print("The number is odd.")




# homework wwednesday august 20th 2025
'''
1. State the 4 properties of a list
2. Give 5 reasons why programmers use lists
3. Differentiate between list indexing and list slicing
4. Create List1 and List2 
List1 has 10, 20, 30, 40, 50
List2 has 60, 70, 80, 60
a.  Check if list list1 does not contain item 12.
b. Creates a new list containing the items from list1 and list2 (concatenate)
c.  Repeat List1 5 times
For both lists:
d.  Get the item at index 3
e.  Count of total items
f.  Removes the first occurrence of item 40
g. Modify the item present at index 2
h. Remove and return the item at index 2 
i. Append the nested list at the end with 2,5,7
j. Return the item with maximum and minimum values
k. Check if lists does not contain item 80
5. Copy list1 into list2
'''

# 1.) state 4 properties of lists
'''
1. Lists are ordered collections of items.
2. Lists can contain items of different data types.
3. Lists are mutable, meaning their contents can be changed.
4. Lists can be nested, meaning a list can contain other lists.
'''
# 2.) give 5 reasons why programmers use lists
'''
1. Lists allow for the storage of multiple items in a single variable.
2. Lists provide an easy way to organize and manipulate data.
3. Lists support various built-in methods for common tasks (e.g., sorting, filtering).
4. Lists can be easily iterated over, making them useful for loops and comprehensions.
5. Lists can be dynamically resized, allowing for flexible data management.
'''
# 3.) differentiate between list indexing and list slicing
'''
- List indexing refers to accessing a single element in a list using its position (index).
- List slicing refers to extracting a sequence of elements from a list by specifying a start and end index, creating a new sublist.
'''
# 4.) create list1 and list2
List1 = [10, 20, 30, 40, 50]
List2 = [60, 70, 80, 60]      

# a. Check if list1 does not contain item 12.
if 12 not in List1:
    print("List1 does not contain 12.")

# b. Creates a new list containing the items from list1 and list2 (concatenate)
List3 = List1 + List2
print("Concatenated List:", List3)

# c. Repeat List1 5 times
List4 = List1 * 5
print("Repeated List1:", List4)

# For both lists:
# d. Get the item at index 3
print("Item at index 3 in List1:", List1[3])
print("Item at index 3 in List2:", List2[3])

# e. Count of total items
print("Total items in List1:", len(List1))
print("Total items in List2:", len(List2))

# f. Removes the first occurrence of item 40
List1.remove(40)
print("List1 after removing 40:", List1)

# g. Modify the item present at index 2
List1[2] = 35
print("List1 after modifying index 2:", List1)

# h. Remove and return the item at index 2
removed_item = List1.pop(2)
print("Removed item from index 2:", removed_item)
print("List1 after removing item at index 2:", List1)

# i. Append the nested list at the end with 2,5,7
List1.append([2, 5, 7])
print("List1 after appending nested list:", List1)

# j. Return the item with maximum and minimum values
# print("Max item in List1:", max(List1))
# print("Min item in List1:", min(List1)) # this does not work 

# k. Check if lists do not contain item 80
if 80 not in List1: 
    print("List1 does not contain 80.")
if 80 not in List2:
    print("List2 does not contain 80.")

# 5. Copy list1 into list2
List2 = List1.copy()
print("List2 after copying List1:", List2)