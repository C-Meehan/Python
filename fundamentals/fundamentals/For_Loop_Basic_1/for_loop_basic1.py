#Basic
for i in range(0,151):
    print(i)

#Multiples of Five
for i in range(5,1001,5):
    print(i)

#Counting, the Dojo Way
for i in range(1,101):
    if (i % 10 == 0):
        print("Coding Dojo")
    elif (i % 5 == 0):
        print("Coding")
    else:
        print(i)

#Whoa. That Sucker's Huge
sum = 0
for i in range(0,500001):
    if (i % 2 != 0):
        sum += i
print(sum)

#Countdown by Fours
i = 2018
while (i >= 0):
    print(i)
    i -=4

#Flexible Counter
lowNum = 2
highNum = 18
mult = 4
for i in range(2,19,4):
    print(i)

#different way to solve last problem
while (lowNum <= highNum):
    print(lowNum)
    lowNum += 4
