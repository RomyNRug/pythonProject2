#Just examples from the Chapter

prefixes = ("JKLMNOPQ")
suffix = "ack"
for p in prefixes:
    print(p + suffix)

greeting = "Hello, world!"
new_greeting = "J" + greeting[1:]
print(new_greeting)

def remove_vowels(phrase):
    vowels = "aeiou"
    string_sans_vowels = ""
    for letter in phrase:
        if letter.lower() not in vowels:
            string_sans_vowels += letter
    return string_sans_vowels

def my_find(haystack, needle):
    for index, letter in enumerate(haystack):
        if letter == needle:
            return index
        return -1

haystack = "Bananarama!"
print(haystack.find('a'))
print(my_find(haystack,'a'))

def count_a(text):
    count = 0
    for letter in text:
        if letter == "a":
            count += 1
            return(count)
print(count_a("banana") == 3)

def find(haystack, needle, start=0, end=-1):
    for index,letter in enumerate(haystack[start:end]):
        if letter == needle:
            return index + start
    return -1

import string
def remove_punctuation(phrase):
    phrase_sans_punct = ""
    for letter in phrase:
        if letter not in string.punctuation:
            phrase_sans_punct += letter
    return phrase_sans_punct

my_story = """ Pythons are constrictors, which means that they will 'squeeze' the life out of their prey. They coil themselves around their prey and with each breath the creature takes the snake will squeeze a little tighter until they stop breathing completely. Once the heart stops the prey swallowed whole. The entire animal is digested in the snake's stomach except for fur or feathers. What do you think happens to the fur, feathers, beaks, and eggshells? The 'extra stuff' gets passed out as --- you guessed it --- snake POOP! """
words = remove_punctuation(my_story).split()
print(words)

phrase = "His name is {0}!".format("Arthur")
print(phrase)
name = "Alice"
age = 10
phrase = "I am {1} and I am {0} years old.".format(age, name)
print(phrase)
phrase = "I am {0} and I am {1} years old.".format(age, name)
print(phrase)

x = 4
y = 5
phrase = "2**10 = {0} and {1} * {2} = {3:f}".format(2**10, x, y, x * y)
print(phrase)

name1 = "Paris"
name2 = "Whitney"
name3 = "Hilton"

print("Pi to three decimal places is {0:.3f}".format(3.1415926))
print("123456789 123456789 123456789 123456789 123456789 123456789")
print("|||{0:<15}|||{1:^15}|||{2:>15}|||Born in {3}|||"
.format(name1,name2,name3,1981))
print("The decimal value {0} converts to hex value {0:x}"
.format(123456))

letter = """Dear {0} {2}.{0}, I have an interesting money-making proposition for you! If you deposit $10 million into my bank account, I ca double your money ..."""

print(letter.format("Paris", "Whitney", "Hilton"))
print(letter.format("Bill", "Henry", "Gates"))

print("i\ti**2\ti**3\ti**5\ti**10\ti**20")
for i in range(1, 11):
    print(i, "\t", i**2, "\t", i**3, "\t", i**5, "\t",i**10, "\t", i**20)

layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"
print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 11):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))


#5.2

