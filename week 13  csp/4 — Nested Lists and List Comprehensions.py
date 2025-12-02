list1 = [1, 2, 3]
print(list1[-1])
list2 = [4, 5, 6]
print(list2[0])
nested_list = [list1, list2] #0 and 1
print(nested_list[0])
print(nested_list[1])
print(nested_list[0][1]) #going inside list 1 through 0 to get 2 from 1
print(nested_list[1][2])
print(nested_list[1][0])

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatos"]
meats = ["chicken", "fish", "turkey"]
groceries = [fruits, vegetables, meats]
print(groceries[2][-1])
print(groceries[1][1])
print(groceries[0][2])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
# #nested loops
# for i in range(1,101): #outer loop
#     for j in range(1,101): #inner loop
#          if i > 0 and j > 0:
#              for k in range(1,101):
#                   print("the number is ", i, j, k)

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))
for row in num_pad:
    for num in row:
        print(num, end="  ")
    print()
# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6

# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]



# Practice Problems:
# Build a matrix variable containing 3 lists of 3 numbers each.
matrix1 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# Print the first list.
print(matrix1[0]) 
# Print the second item from the third list.
print(matrix1[2][1]) 
# Use a list comprehension to extract the last item from each sub-list.
sum_list = [row[-1] for row in matrix1]
print(sum_list)
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
squares = [x**2 for x in range(1,11)]
for x in range(1,11):
    print(x**2)
print(squares)