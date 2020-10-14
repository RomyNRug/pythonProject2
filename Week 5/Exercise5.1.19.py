#1 Python Console

#2

prefixes = ("JKLMNOPQ")
suffix = "ack"
for letter in prefixes:
    if letter == "O" or letter == "Q":
        print (letter + "u" + suffix)
    print (letter + suffix)

#3
word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count += 1
    print(count)

def count_letter(letter,string):
    count=0
    for character in string:
        if character == letter:
            count=+ 1
    return count
 #4 ???

 #5
poem= "A million stars up in the sky. One shines brighter - I cant deny. A love so precious, a love so true, a love that comes from me to you."
part1= poem[0:15]
part2= poem[16:30]
part3= poem [31:20000]
print(part1+ part2+part3)

e_words = 0
for word in poem:
    if "e" in word:
        e_words += 1
    total_words = len(poem)
    e_percent = e_words * 100 / total_words
    template = 'Your text contains {0} words, ' \
        'of which {1} ({2:.2f}%) contain an "e".'
print(template.format(total_words, e_words, e_percent))

#6 COME BACK LATER TO FINISH
print("i\ti**2\ti**3\ti**5\ti**10\ti**20")
for i in range(1, 11):
    print(i, "\t", i*2, "\t", i*3, "\t", i*4, "\t",i*5, "\t", i*6, "\t", i*7,"\t", i*8,"\t", i*9,"\t", i*10)

#7
def reverse(string):
    string= string[::-1]
    return string

#8
def mirror(string):
    return string + string[::-1]

#9
def remove_string(letter,string):
    string= ""
    for character in string:
        if character != letter: #! is not equal to, dont forget
            string= string+ character
    return string

#10
def is_palindrome(string):
    return string == reverse(string)

#11
#???

#12 till 13 are very unclear










