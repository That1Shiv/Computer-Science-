# import math

# #question 1 
# x = 300
# y = 330

# if y > x:
#   print('y is greater than x')
# else:
#   print('y is not greater than x')

# # #question 2
# name = input('what is your name? ')
# age = input('What is your age? ')
# height = input('what is your height? ')
# weight = input('what is your weight? ')

# print("Your details are:")
# print("Name:", name)
# print("Age:", age)
# print("Height:", height)    
# print("Weight:", weight)

# # #question 3 

# food = input('What is your favourite food?  ')
# name = input('What is your name? ')

# print(name + ' likes ' + food)


# # # question 4 

# name = input('what is your name? ')
# age = input('what is your age? ')
# school = input('What school do you go to? ')

# print(name + ' is ' + age + ' and goes to ' + school + ' school ')

# --- reverse list at location ---
# #question 5 (reverse order)
# first_name = input('Enter your first name: ')
# last_name = input('Enter your last name:    ')
# print(last_name + ' ' + first_name)

# # question 6 
# n = input("Enter an integer: ")
# result = int(n) + int(n*2) + int(n*3)
# print("Result:", result)
# --- find largest element in list ---

# # question 7
# radius = 6
# volume = (4/3) * math.pi * radius**3
# print("The volume of the sphere is:", volume)

# # question 8 
# number = int(input("Enter a number: "))
# if number % 2 == 0:
# --- union and intersection of lists ---
#   print("The number is even.")
# else:
#   print("The number is odd.")




# # homework wwednesday august 20th 2025
# '''
# 1. State the 4 properties of a list
# 2. Give 5 reasons why programmers use lists
# 3. Differentiate between list indexing and list slicing
# --- first non-repeated element in list ---
# 4. Create List1 and List2 
# List1 has 10, 20, 30, 40, 50
# List2 has 60, 70, 80, 60
# a.  Check if list list1 does not contain item 12.
# b. Creates a new list containing the items from list1 and list2 (concatenate)
# c.  Repeat List1 5 times
# For both lists:
# d.  Get the item at index 3
# e.  Count of total items
# f.  Removes the first occurrence of item 40
# g. Modify the item present at index 2
# h. Remove and return the item at index 2 
# --- sum all items in list ---
# i. Append the nested list at the end with 2,5,7
# j. Return the item with maximum and minimum values
# k. Check if lists does not contain item 80
# 5. Copy list1 into list2
# '''

# # 1.) state 4 properties of lists
# '''
# 1. Lists are ordered collections of items.
# --- find smallest number in list ---
# 2. Lists can contain items of different data types.
# 3. Lists are mutable, meaning their contents can be changed.
# 4. Lists can be nested, meaning a list can contain other lists.
# '''
# # 2.) give 5 reasons why programmers use lists
# '''
# 1. Lists allow for the storage of multiple items in a single variable.
# 2. Lists provide an easy way to organize and manipulate data.
# 3. Lists support various built-in methods for common tasks (e.g., sorting, filtering).
# --- check if list is empty ---
# 4. Lists can be easily iterated over, making them useful for loops and comprehensions.
# 5. Lists can be dynamically resized, allowing for flexible data management.
# '''
# # 3.) differentiate between list indexing and list slicing
# '''
# - List indexing refers to accessing a single element in a list using its position (index).
# - List slicing refers to extracting a sequence of elements from a list by specifying a start and end index, creating a new sublist.
# '''
# # 4.) create list1 and list2
# List1 = [10, 20, 30, 40, 50]
# --- remove elements by index ---
# List2 = [60, 70, 80, 60]      

# # a. Check if list1 does not contain item 12.
# if 12 not in List1:
#     print("List1 does not contain 12.")

# # b. Creates a new list containing the items from list1 and list2 (concatenate)
# List3 = List1 + List2
# print("Concatenated List:", List3)
# --- shuffle list ---

# # c. Repeat List1 5 times
# List4 = List1 * 5
# print("Repeated List1:", List4)

# # For both lists:
# # d. Get the item at index 3
# print("Item at index 3 in List1:", List1[3])
# print("Item at index 3 in List2:", List2[3])

# # e. Count of total items
# print("Total items in List1:", len(List1))
# --- get indices of list ---
# print("Total items in List2:", len(List2))

# # f. Removes the first occurrence of item 40
# List1.remove(40)
# print("List1 after removing 40:", List1)

# # g. Modify the item present at index 2
# List1[2] = 35
# print("List1 after modifying index 2:", List1)
# --- append one list to another ---

# # h. Remove and return the item at index 2
# removed_item = List1.pop(2)
# print("Removed item from index 2:", removed_item)
# print("List1 after removing item at index 2:", List1)

# # i. Append the nested list at the end with 2,5,7
# List1.append([2, 5, 7])
# print("List1 after appending nested list:", List1)

# --- get unique values from list ---
# # j. Return the item with maximum and minimum values
# # print("Max item in List1:", max(List1))
# # print("Min item in List1:", min(List1)) # this does not work 

# # k. Check if lists do not contain item 80
# if 80 not in List1: 
#     print("List1 does not contain 80.")
# if 80 not in List2:
#     print("List2 does not contain 80.")
# --- count elements in range ---

# # 5. Copy list1 into list2
# List2 = List1.copy()  
# print("List2 after copying List1:", List2)



# ###############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
# Example lists for use
# --- sum all items in list (repeat) ---
# numbers = [1, 2, 3, 4, 5]
# fruits = ['apple', 'banana', 'cherry', 'date']
# mixed = [10, 'hello', 3.14, True, None]



# --- multiply all items in list ---
# # 1.) Create a python function to reverse a list at a specific location 
# def reverse_list_at_index(lst, index):
#     if index < 0 or index >= len(lst):
#         return "Index out of range"
#     return lst[:index] + lst[index:][::-1]
# print(reverse_list_at_index(mixed, 2))

# # 2.) write a python function to find the largest element in a list 
# def Find_biggest_in_list(list):
#     if not list:
#         return 'list is empty'
#     largest = list[0]
# --- remove duplicates from list ---
#     for num in list:
#         if num > largest:
#             largest = num
#     return largest
# print(Find_biggest_in_list(numbers))
# # 3.) write a python function to find the union and intersection of 2 lists

 
# # 4.) write a python program to find the first non repeated element in a list 
# def first_non_repeated(list):
#     for item in list:
#         if list.count(item) == 1:
#             return item
#     return None
# repeated_list = [1, 2, 3, 2, 1, 4, 5]
# print(first_non_repeated(repeated_list))

# # 5.) write a python program to sum all the items in a list
# def sum_of_list(lst):
#     total = sum(lst)
#     return total 
# # 6.) write a python program to get the smallest number from a list
# def find_smallest(list):
#     if not list:
#         return 'list is empty' 
#     smallest = list[0]
#     for num in list:
#         if num < smallest:
#             smallest = num
#     return smallest
# print(find_smallest(numbers))

# # 7.) write a python program to check if a list is empty or not
# def is_list_empty(numbers):
#     return len(numbers) == 0
# # 8.) write a python program too print a specified list after removing the 0th, 4th, and 5th elements

# # 9.) Write a python  program to shuffle and print a specified list

# # 10.) write a python program to access the index of a list 

# # 11.) write a python program to append a list to the second list
# def append_lists(numbers, fruits):
#     numbers.extend(fruits)
#     return numbers
# # 12.) write a python program to get unique values from a list 

# # 13.) write a python program to count the number of elements ina  list with a specifed range. 


# # 14.) Write a python program to sum all the items in a list
# def sum_of_list(numbers):
#     total = sum(numbers)
#     return total
# # 15.) write a python program to multiply all the items in a list 
# def multiply_list(list):
#     result = 1 
#     for num in list:
#         result *= num
#         return result

# # 16.) Write a python program to remove duplicates from a list 
















# Tuesday August 26th 2025 



# Create a Tuple: Create a tuple named my_tuple containing the numbers 1, 2, 3, 4, and 5.

# Access Elements: Access and print the third element of my_tuple.

# Tuple Length: Find and print the length of my_tuple.
# Repeat a below tuple three times

# Slice below tuple to get elements from the 4th to the 7th position.
# Given: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13)

# Reverse the tuple
# Given: tuple1 = (10, 20, 30, 40, 50)

# Write a code to unpack the following tuple into four variables and display each variable.
# Given: tuple1 = (10, 20, 30, 40)

# my_tuple = (1,2,3,4,5)
# print(my_tuple[2])
# print(len(my_tuple))
# print(my_tuple * 3)

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13)
# print(numbers[3:7])

# tuple1 = (10, 20, 30, 40, 50)
# print(tuple1[::-1])    

# tuple2 = (10, 20, 30, 40)


# thursday 28th august 2025

# write a python function that takes a list of words and return the longest word and the length of the longest one
def find_longest_word(words):
    if not words:
        return None, 
    longest_word = max(words, key=len)
    return longest_word, len(longest_word)
# print(find_longest_word(["a","bb","ccc",]))


# write a python program to find the first appearance of the substrings 'not' and 'poor' in a given string. if 'not' follows 'poor', replace the whole 'not'...poor substring with 'good'. return the resulting string 

def replace_not_poor(text):
    words = text.split()

    if "not" in words and "poor" in words: 
        not_index = words.index("not")
        poor_index = words.index('poor')

        if not_index < poor_index: 
            words[not_index:poor_index+1] = ["good"]

    return " ".join(words) 
# print(replace_not_poor("The food is not that poor"))

# write a python program to get a single string from two given strings, seperated by a space and swap the first two characters of each string 
 
def swap_strings(a,b): 
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + " " + new_b
# print(swap_strings("abc","xyz"))

# write a python function to find the union and intersection fo two lists
def union_and_intersection(list1, list2):
    union = list(set(list1) | set(list2))
    intersection = list(set(list1) & set(list2))
    return union, intersection
# print(union_and_intersection([1,2,3,4],[3,4,5,6]))

# write a python program to print a tuple with string formatting
####### 
######
######
###### 

# write a python program to convert a tuple to a string