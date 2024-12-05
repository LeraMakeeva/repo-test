x = 756237282
last = 0
minimum = 9
maximum = 0
while x > 0:
    last = x % 10
    x = x // 10
    if last < minimum:
        minimum = last
    if last > maximum:
        maximum = last
print(maximum)
print(minimum)
