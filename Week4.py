# Strings

# Can use single or double quotes
from typing import List, Any

name = "Sasha"
color = 'red'

# We can multiply strings by a number
# That will repeat the string n times

print("ana" * 3)

# To know the length of a string

print(len("Ana"))

minombre = "Ana"

# Access a position in the string

print(minombre[0])
print(minombre[-1])

# Accessing a range of characters
color2 = "Orange"

print(color2[1:4])

fruit = "Pineapple"

print(fruit[:4])  # from start to pos 3
print(fruit[4:])  # from pos 4 to end

# strings in python are immutable = cannot be changed

# Fixing a typo

message = "A kong string with a silly typo"

new_message = message[0:2] + "l" + message[3:]
print(new_message)

# String methods

pets = "Cats & Dogs"

print(pets.index("&"))

# To verify if a word/letter is in a string

print("Cats" in pets)


# Example to replace an e-mail domain

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


# More string methods

# Changing all letters to Upper

print("Mountains".upper())

# Changing all letters to lower

print("Mountains".lower())

# Strip method - erases surrounding spaces in strings
# .lstrip - spaces in the left
# .rstrip - spaces in the right

print(" yes ".strip())

# Count method - counts how many time a letter/word/symbol appears in a string

print("The number of times e occurs in this string is 4".count("e"))

# .isnumeric - tells if a variable is a number

print("Forest".isnumeric())
print("1234".isnumeric())

# .join - adding parts of a string

print(" ".join(["This", "is", "a", "phrase"]))
print("...".join(["This", "is", "a", "phrase", "with", "triple", "dots"]))

# .split - returns a list with the words in a string

print("This is another string".split()[-1])  # ['This', 'is', 'another', 'string']


def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result


print(initials("Universal Serial Bus"))  # Should be: USB
print(initials("local area network"))  # Should be: LAN
print(initials("Operating system"))  # Should be: OS


# .format

def student_grade(name, grade):
    return "{} received {}% on the exam".format(name, grade)


print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

# another example of .format

price = 7.5
with_tax = price * 1.09
print("Base price ${:.2f}. With tax: ${:.2f}".format(price, with_tax))


# another example

def to_celsius(x):
    return (x - 32) * 5 / 9


for x in range(0, 101, 20):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

input_string = "hola"

for letter in input_string:
    print(letter)


def is_palindrome(input_string):
    # created two empty strings, to compare them
    new_string = ""
    reverse_string = ""
    # traversing through each letter of input string
    for i in input_string:
        if i != "":
            # adding non blank letters to end of new_string
            new_string = new_string.strip() + i
            # adding non blank letters to start of reverse_string
            reverse_string = i + reverse_string.strip()
    # Compare the strings
    if new_string.lower() == reverse_string.lower():
        return True
    return False


print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True


# lists

def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return (words[n - 1])
    return ("")


print(get_word("This is a lesson about lists", 4))  # Should print: lesson

# Modifying elements in a list

# append method

fruits = ["Pineapple", "Banana", "Apple", "Melon"]

fruits.append("kiwi")  # ["Pineapple", "Banana", "Apple", "Melon", "kiwi"]

fruits.insert(0, "orange")  # ["Orange", "Pineapple", "Banana", "Apple", "Melon", "kiwi"]

fruits.remove("Melon")

fruits.pop(3)  # Apple

# Strings - sequences of characters and are INMUTABLE

# Lists - sequences of elements of any type, and are MUTABLE

# Tuple - sequences of elements of any type, that are INMUTABLE

fullname = ('Grace', 'M', 'Hopper')


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


result = convert_seconds(5000)
print(type(result))
print(result)

# Spliting the elements of teh tuple into separate variables

hours, minutes, seconds = convert_seconds(1000)
print (hours, minutes, seconds)


# Example using tuples, store information about a file: its name, its type and its size in bytes

def file_size(file_info):
    name, type, size = file_info
    return "{:.2f}".format(size / 1024)


print(file_size(('Class Assignment', 'docx', 17875)))

# Iterating over Lists and Tuples

animals = ["lion", "Zebra", "Dolphin", "Monkey"]
chars = 0

for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars / len(animals)))

# Using index

winners = ["Ashley", "Dylan", "Reese"]

for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


# Example - using index - exercise 1

def skip_elements(elements):
    result = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            result.append(element)

    return result


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']

# Example - using index - exercise 2

def full_emails(people):
    result = []

    for name, email in people:
        result.append("{} - <{}>".format(name, email))
    return result


print(full_emails([()]))
