# Following mosh's lecture 5.12:

list1 = [1, 2, 3]
list2 = [4, 5, 6]

zipList = zip(list1, list2)

# Using list() to convert a zip object into a list
print(list(zipList))

# output is: [(1, 4), (2, 5), (3, 6)]
