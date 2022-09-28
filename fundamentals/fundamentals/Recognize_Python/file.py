num1 = 42 #variable declaration. Primitive Numbers
num2 = 2.3 #variable declaration. Primitive Numbers
boolean = True #Primitive Boolean
string = 'Hello World' #Primitive String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list initilize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary initilize
fruit = ('blueberry', 'strawberry', 'banana') #tuple initilize
print(type(fruit)) #type check
print(pizza_toppings[1]) #list access value
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) #dictionary access value
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary add value
print(fruit[2]) #tuple access value

if num1 > 45: #conditional if statement
    print("It's greater") #print string
else: #conditional else statement
    print("It's lower") #print string

if len(string) < 5: #conditional if statement. length of string check
    print("It's a short word!") #print string
elif len(string) > 15: #conditional else if statement for length of string
    print("It's a long word!") #print statement
else: #conditional else statement
    print("Just right!") #print string

for x in range(5): #for loop. start and increment through 5
    print(x) #print 0 through 5
for x in range(2,5): #for loop. start at 2 and increment through 5
    print(x) #print 2 - 5
for x in range(2,10,3): #for loop. ??????
    print(x) #print x????
x = 0
while(x < 5): #while loop.
    print(x) #print x while under 5
    x += 1 #x increment plus 1

pizza_toppings.pop() #takes off last value from pizza_toppings
pizza_toppings.pop(1) #takes off pizza_toppings[1]

print(person) #prints person dictionary
person.pop('eye_color') #takes off 'eye_color' from dictionary
print(person) #prints new value for person

for topping in pizza_toppings: #start of for loop
    if topping == 'Pepperoni': #conditional if statement. if topping is 'Pepperoni'
        continue #continue to next step in loop if previous if statement is true
    print('After 1st if statement') #prints only if 1st if statement is true
    if topping == 'Olives': #conditional if statement. if topping is 'Olives'
        break #break away from loop

def print_hello_ten_times(): #declaring a function
    for num in range(10): #for loop through 10
        print('Hello') #print string

print_hello_ten_times() #calls function to run 

def print_hello_x_times(x): #declaring a function with a parameter
    for num in range(x): #for loop through the amount of argument passed
        print('Hello') #print string

print_hello_x_times(4) #calling function with argument 

def print_hello_x_or_ten_times(x = 10): #declaring function with set parameter
    for num in range(x): #for loop through amount of argument
        print('Hello') #print string

print_hello_x_or_ten_times() #calling function
print_hello_x_or_ten_times(4) #calling function with argument


"""
Bonus section
"""

# print(num3) #NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry' change value
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7]) #IndexError: list index out of range
#   print(boolean) #IndentationError: unexpected indent
# fruit.append('raspberry') #add value
# fruit.pop(1) #delete value