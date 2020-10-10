# Strings

# Can use single or double quotes
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