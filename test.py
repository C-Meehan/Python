# import random
# print(random.randint(2,5)) # provides a random number between 2 and 5


# print ("hello world")

# # Conversions for python

# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))

# #Find types
# print(type(24))
# print(type(3.9))
# print(type(3j))

# #F-string example
# first_name = "Chris"
# last_name = "Meehan"
# age = 31
# print(f"My name is {first_name} {last_name} and I am {age} years old.")

# #string.format() example
# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# # output: My name is Zen Coder and I am 27 years old.
# print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# # output: My name is 27 Zen and I am Coder years old.

# # %-formatting (pretty old, probably won't use)
# hw = "Hello %s" % "world" 	# with literal values
# py = "I love Python %d" % 3 
# print(hw, py)
# # output: Hello world I love Python 3
# name = "Zen"
# age = 27
# print("My name is %s and I'm %d" % (name, age))		# or with variables
# # output: My name is Zen and I'm 27

# fruits = ['apple', 'banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucumber', 'carrots']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)
# salad = 3 * vegetables
# print(salad)

# age = 31
# print(type(age))
# age = str(age)
# print(type(age))

#Slicing examples
# words = ["start","going","till","the","end"]
# # Sub-ranges (portions) of the list
# print(words[1:]) # prints ['going', 'till', 'the', 'end']
# print(words[:4]) # prints ['start', 'going', 'till', 'the']
# print(words[2:4]) # prints ['till', 'the']
    
# # Making a copy of a list
# copy_of_words = words[:]
# copy_of_words.append("dojo") # only appends to the copy
# print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
# print(words) # prints ['start', 'going', 'till', 'the', 'end']

# num = ['dave','chris','4']
# num.sort()
# print(num)

# #Print debugging practice w/solution at end
# def multiply(num_list, num):
#     print(num_list, num)
#     for x in num_list:
#         print(x)
#         x *= num
#         print(num_list)
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)

# def multiply(num_list,num):
#     for x in range(len(num_list)):
#         num_list[x] *= num
#     return num_list
# a = [2,4,10,16]
# b = multiply(a,5)
# print(b)

# #literal notation
# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# #A different way to create dictionary
# capitals = {} #create an empty dictionary then add values
# capitals["svk"] = "Bratislava"
# capitals["deu"] = "Berlin"
# capitals["dnk"] = "Copenhagen"

# value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
# del capitals['dnk'] # will delete the key, and not return anything


# person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# # Adds a new key value pair for email to person
# person["email"] = "alovelace@codingdojo.com"
        
# # Changes person's "last" value to "Bobada"
# person["last"] = "Bobada"
# print(person)
# full_name = person["first"] + " " + person["last"]
# print(full_name)

# #person.clear() will clear entire dictionary

# capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# # another way to iterate through the keys
# for key in capitals.keys():
#      print(key)
# # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# #to iterate through the values
# for val in capitals.values():
#      print(val)
# # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# #to iterate through both keys and values
# for key, val in capitals.items():
#      print(key, " = ", val)
# # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# List of dictionaries
# users = [
#     {"first": "Ada", "last": "Lovelace"}, # index 0
#     {"first": "Alan", "last": "Turing"}, # index 1
#     {"first": "Eric", "last": "Idle"} # index 2
# ]
# # Dictionary of lists
# resume_data = {
#     #        	     0           1           2
#     "skills": ["front-end", "back-end", "database"],
#     #                0           1
#     "languages": ["Python", "JavaScript"],
#     #                0              1
#     "hobbies":["rock climbing", "knitting"]
# }

# print(resume_data["skills"][1])
# print(users[2]["first"])
