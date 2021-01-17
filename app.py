# Following mosh's lecture 5.23: Exercise:

sentence = "This is a common interview question"
# I need to find the most repeated character in the text:

# first make a list which contains all the characters as it is
list_0f_all_characters = list(sentence)

print(list_0f_all_characters)

# second, make a set of all the characters
set_0f_all_characters = set(list_0f_all_characters)
print(set_0f_all_characters)

# remove the blank space from the empty character
set_for_blank_space = {" "}

set_0f_all_characters_wo_blank_space = set_0f_all_characters - set_for_blank_space

print(set_0f_all_characters_wo_blank_space)

# third, loop over all the characters in the set and count occurrences
# of each character.
# when we are looping over, we should also store the unique character and
# its number of occurrences as a dictionary

character_array = []
character_count_array = []
for character in set_0f_all_characters_wo_blank_space:
    character_count = list_0f_all_characters.count(character)
    character_array.append(character)
    character_count_array.append(character_count)

key_count_pair_tuple = tuple(zip(character_array, character_count_array))

# Finally, printout the character which has the largest count

# print(len(key_count_pair_tuple))
# print(key_count_pair_tuple)
sortedList = sorted(key_count_pair_tuple,
                    key=lambda item: item[1], reverse=True)
print(sortedList)

print("The character with maximum number of occurrences is " +
      sortedList[0][0])
