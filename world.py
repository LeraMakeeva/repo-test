x = int(input())
last = 0
minimum = 9

while x > 0:
    last = x % 10
    x = x // 10
    if last < minimum:
        minimum = last

print(minimum)
