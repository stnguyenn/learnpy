



x = int(input("Please enter an integer: "))
# Please enter an integer: 42
if x < 0:
     x = 0
     print('Negative changed to zero')
elif x == 0:
     print('Zero')
elif x == 1:
     print('Single')
else:
     print('More')

# More

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
     print(w, len(w))

# cat 3
# window 6
# defenestrate 12

for w in words[:]:  # Loop over a slice copy of the entire list.
     if len(w) > 6:
         words.insert(0, w)

words
['defenestrate', 'cat', 'window', 'defenestrate']

for i in range(5):
     print(i)

0
1
2
3
4

range(5, 10)
#    5, 6, 7, 8, 9

range(0, 10, 3)
#    0, 3, 6, 9

range(-10, -100, -30)
#   -10, -40, -70

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
     print(i, a[i])

# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb


print(range(10))
range(0, 10)


list(range(5))
[0, 1, 2, 3, 4]

for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # loop fell through without finding a factor
         print(n, 'is a prime number')

# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3

for num in range(2, 10):
     if num % 2 == 0:
         print("Found an even number", num)
         continue
     print("Found a number", num)
# Found an even number 2
# Found a number 3
# Found an even number 4
# Found a number 5
# Found an even number 6
# Found a number 7
# Found an even number 8
# Found a number 9

# while True:
    #  pass  # Busy-wait for keyboard interrupt (Ctrl+C)


class MyEmptyClass:
     pass


def initlog(*args):
     pass   # Remember to implement this!


