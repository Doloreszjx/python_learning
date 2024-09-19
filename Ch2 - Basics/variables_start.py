#
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "three", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one": 1, "two": 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
myint = 15
print('re-declaring myint: ', myint)
# to access a member of a sequence type, use []
third_ele_mylist = mylist[2]
print('access the third element in the mylist: ', third_ele_mylist)
# use slices to get parts of a sequence
get_2to4_ele = mystr[1:4]
print('get 2 to 4 elements from mystr: ', get_2to4_ele)
# you can use slices to reverse a sequence
reverse_str = mystr[::-1]
reverse_list = mylist[::-1]
print('reverse mystr: ', reverse_str)
print('reverse mylist:', reverse_list)
# dictionaries are accessed via keys
dic_one = mydict.get("one")
dic_two = mydict['two']
print('get the value of the first key in mydict: ', dic_one)
print('get the value of the second key in mydict: ', dic_two)
# ERROR: variables of different types cannot be combined
# TypeError: can only concatenate str (not "int") to str
# print('string type ' + 123)
print('string type: ' + str(123))
# Global vs. local variables in functions


def update_mytuple():
    mytuple = (2, 9, 'func_tuple')
    print('local scope: ', mytuple)


update_mytuple()
print('global scope: ', mytuple)
