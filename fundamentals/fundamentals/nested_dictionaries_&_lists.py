# 1.Update Valies in Dictionaries and Lists
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

x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] = 30

print(x)
print(students)
print(sports_directory)
print(z)

# 2.Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    output_list = []
    for some_dict in some_list:
        entry = ""
        for key,value in some_dict.items():
            entry += key + ' - ' + value + ', '
        entry = entry[:-2]
        output_list.append(entry)
    for element in output_list:
        print(element)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
"""
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
"""


# 3.Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for some_dict in some_list:
        print(some_dict[key_name])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)


# 4.Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for some_list in some_dict:
        print(len(some_dict[some_list]), some_list.upper())
        for element in some_dict[some_list]:
            print(element)
        print("")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
# output:
"""
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""