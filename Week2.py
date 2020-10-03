var2 = 5
var = 2

print(var + var2)


# Defining functions

def greeting(name, department):
    print("Welcome " + name)
    print("You are part of " + department)


greeting("Ana", "Front-End Development")


# Return values

def area_triangle(base, height):
    return base * height / 2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)


def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + " your lucky numer is " + str(number))


lucky_number("Ana")
lucky_number("Kay")

# comparations

print(10 > 1)
print("cat" == "dog")
print(1 != 2)
print("cat" > "Cat")

# logical operators

print("Yellow" > "Cyan" and "Brown" > "Magenta")
print(25 > 50 or 1 != 2)
print(not 42 == "Answer")


# Branching

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")


hint_username("Ana")


def is_even(number):
    if number % 2 == 0:
        return True
    return False


print(is_even(3))


# Elif statement

def hint_username2(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username: Must be at most 15 characters long")
    else:
        print("Valid username")

print("big" > "small")
