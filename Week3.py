# while loops


x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")


attempts(5)


def sum_divisors(n):
    sum = 0
    # Return the sum of all divisors of n, not including n
    div = 1
    while div < n:
        if n % div == 0:
            sum = sum + div
        div = div + 1
    return sum


print(sum_divisors(0))
# 0
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# 114


# for loop

for x in range(5):
    print(x)

friends = ['Taylor', 'Alex', 'Pat', 'Eli']

for friend in friends:
    print("Hi " + friend)

# nested for loops
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()