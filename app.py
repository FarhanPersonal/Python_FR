# Following mosh's lecture 5.18:

numbers = [1, 2, 3, 2, 3]

firstSet = set(numbers)

secondSet = {3, 4, 5}

# priting union of two sets
print(firstSet | secondSet)

print("printing common", firstSet & secondSet)

print("printing either", firstSet ^ secondSet)
