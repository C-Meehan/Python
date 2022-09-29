x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#1 Update Values
#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]
x[1][0] = 15
print(x)
#Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students[0])
#In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
#Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

#2 Iterate through list of dictionaries
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(list):
    # for persons in list:
    #     print(persons)
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val},"
        print(output)
        
iterateDictionary(students)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#3 Get Values From a List of Dictionaries
def iterateDictionary2(key_name,list):
    for i in range(0,len(list)):
        for key,val in list[i].items():
            if key == key_name:
                print(val)

iterateDictionary2("first_name",students)
iterateDictionary2("last_name",students)

# 4 Iterate Through a Dictionary with List Values
# loop through dictionary
# loop through key 
# get values of key
# keep track of number of values
# print number of values plus the name of key
# print values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dictionary):
    for key in dictionary:
        print(len(dictionary[key]), key)
        for val in dictionary[key]:
            print(val)
            
printInfo(dojo)