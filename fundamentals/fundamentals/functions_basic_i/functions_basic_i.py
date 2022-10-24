#1
def number_of_food_groups():
    return 5
# print 5
print(number_of_food_groups())

#3
def number_of_books_on_hold():
    return 5
    return 10
# print 5
print(number_of_books_on_hold())


#4
def number_of_fingers():
    return 5
    print(10)
# print 5
print(number_of_fingers())


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
# print 5, print None
print(x)


#6
def add(b,c):
    print(b+c)
# print 3, print 5, TypeError for attempting to add two values of type None
print(add(1,2) + add(2,3))


#7
def concatenate(b,c):
    return str(b)+str(c)
# print 25
print(concatenate(2,5))


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
# print 100, print 10
print(number_of_oceans_or_fingers_or_continents())


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
# print 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print 21
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#2
def number_of_military_branches():
    return 5
# TypeError for number_of_days_in_a_week_silicon_or_triangle_sides() since it is missing the 2 required arguments
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#10
def addition(b,c):
    return b+c
    return 10
# print 8
print(addition(3,5))


#11
b = 500
# print 500
print(b)
def foobar():
    b = 300
    print(b)
# print 500
print(b)
# print 300
foobar()
# print 500
print(b)


#12
b = 500
# print 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
# print 500
print(b)
# print 300
foobar()
# print 500
print(b)


#13
b = 500
# print 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
# print 500
print(b)
# print 300
b=foobar()
# print 300
print(b)


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
# print 1, print 3, print 2
foo()


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
# print 1, print 3, print 5
y = foo()
# print 10
print(y)