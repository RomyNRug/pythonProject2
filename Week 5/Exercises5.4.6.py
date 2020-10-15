#1
def count_letters(text):
    letter_counts = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter not in letter_counts:
                letter_counts[letter] = 1
            else:
                letter_counts[letter] += 1
    return letter_counts


def print_letter_counts(letter_counts):
    for letter in sorted(letter_counts):
        print(letter, letter_counts[letter])


input_text = "ThiS is String with Upper and lower case Letters"
print_letter_counts(count_letters(input_text))

#2
def add_fruit(inventory, fruit, quantity=0):
    if fruit not in inventory:
        inventory[fruit] = quantity
    else:
        inventory[fruit] += quantity


new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print(new_inventory)
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory)

#3
#????

#4
for words in (alice.txt):
    if len(longwords)>len(words):
        longwords=words
    print("the longest word is ",longwords, ".")