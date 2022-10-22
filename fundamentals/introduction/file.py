num1 = 42 # variable declaration, initialize number
num2 = 2.3 # variable declaration, initialize number
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initalize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initalize tuple
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, access value from list
pizza_toppings.append('Mushrooms') # add value to list 
print(person['name']) # log statement, accss value from person
person['name'] = 'George' # change value in dictionary
person['eye_color'] = 'blue' # add value to dictionary
print(fruit[2]) # log statement, access value from tuple

if num1 > 45: # if statement 
    print("It's greater") # log statement
else: # else statement
    print("It's lower") # log statement

if len(string) < 5: # if statement, function to return length of string
    print("It's a short word!") # log statement
elif len(string) > 15: # else if statement, function to return length of string
    print("It's a long word!") # log statement
else: # else statement
    print("Just right!") # log statement

for x in range(5): # for loop, stop argument
    print(x) # log statement
for x in range(2,5): # for loop, start argument, stop argument
    print(x) # log statement
for x in range(2,10,3): # for loop, start argument, stop argument, increment argument
    print(x) # log statement
x = 0 # variable declaration, initialize number
while(x < 5): # while loop, stop condition
    print(x) # log statement
    x += 1 # increment statement

pizza_toppings.pop() # function to remove last element from list
pizza_toppings.pop(1) # function to remove 2nd element from list

print(person) # log statement
person.pop('eye_color') # function to remove designated key from dictionary
print(person) # log statement

for topping in pizza_toppings: # for loop 
    if topping == 'Pepperoni': # if statement
        continue # continue statement
    print('After 1st if statement') # log statement
    if topping == 'Olives': # if statement
        break # break statement

def print_hello_ten_times(): # function definition
    for num in range(10): # for loop, stop argument
        print('Hello') # log statement

print_hello_ten_times() # log statement

def print_hello_x_times(x): # function definition, one parameter
    for num in range(x): # for loop, function parameter set as stop argument
        print('Hello') # log statement

print_hello_x_times(4) # log statement

def print_hello_x_or_ten_times(x = 10): # function definition, one parameter assigned w/ default value
    for num in range(x): # for loop, function parameter set as stop argument
        print('Hello') # log statement

print_hello_x_or_ten_times() # funciton call
print_hello_x_or_ten_times(4) # function call


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)