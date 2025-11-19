# sets and tuples examples:
#sets examples:

set1 = {1, 2, 3, 4, 5}
print(set1) # {1, 2, 3, 4, 5}
print(type(set1)) # <class 'set'>
set1.add(6)
print(set1) # {1, 2, 3, 4, 5}
set1.remove(2)
print(set1) # {1, 2, 3, 4, 5}

# set drops duplicate items:
set2 = {"apple", "banana", "cherry", "cherry"}
print(set2) # {'apple', 'banana', 'cherry'}

#tuples examples:
tuple1 = (1, 2, 3, 4, 5,)
print(tuple1) # (1, 2, 3, 4, 5)
print(type(tuple1)) # <class 'tuple'>
#tuples are immutable, meaing they cannot be changed after creation
# this makes tuples useful for storing data that should not be modified 
social_security_number = (123444, 4444445, 5676789)
print(social_security_number) # (123444, 4444445, 5676789)
