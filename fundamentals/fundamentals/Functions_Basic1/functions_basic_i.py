# def number_of_days_in_a_week_silicon_or_triangle_sides():
#     pass

#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#prediction 5


#2
def number_of_military_branches():
    return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#prediction error. to fix you need to define the function first or just comment out the line to continue


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#prediction 5. first return holds true and kicks out of function

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#prediction 5. function holds value of 5. return kicks out of function


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#prediction 5 then none. prints 5 since function was called. printing x prints nothing since the value of x is nothing because return value absent


#6
def add(b,c):
    print(b+c)
# print(add(1,2) + add(2,3))
#prediction 3,5,8. wrong its 3,5,error. can't add two of the same function in one print statement


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#prediction 25. turns into string thereforse combined like string. '2' +'5' = 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#prediction 100,10. prints value of b which = 100 then goes to else statement since bigger than 10. returns 10 as value. leaves function


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#prediction 7,14,21 executes all three calls. 1st returns 7 bc of if. 2nd returns 14 bc of else.3rd adds both together


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#prediction 8. runs function which adds the arguments and returns value


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#prediction 500,500,300,500. prints b then prints b again. runs function which prints b which equals 300 in function. then prints b which is still 500 outside of function


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#prediction 500,500,300,500. same as before. foobar now has value of 300 but was not called upon after that


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#prediction 500,500,300,300. first two print 500 as b, then function runs and prints 300. function is now = to 300. b now = function (which is equal to 300) printing b now results in 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#prediction 1,3,2 foo is invoked and prints 1, then bar is invoked inside of foo. bar prints 3, then print 2 is next


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#prediction 1,3,5,10. y is set to foo() which invokes the function. prints 1, then x is set to bar() which invokes function. prints 3 and bar() returns with a value of 5 which x is not set to. prints x which is now 5. then returns 10

