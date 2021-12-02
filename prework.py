#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
#The first line of the code has been defined as below.
def hello_name(user_name):
    print("hello_" + user_name.upper() +"!")
hello_name('juggernaut')

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for num in range(1,100):
        if num % 2 != 0:
            print(num)

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.
def max_num_in_list(a_list):
    for max_num in mylist:
        return max(mylist)
mylist = [1,2,3,4]
print(max_num_in_list(mylist))

#Question 4
#Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return a_year, "is a leap year"
            else:
                return a_year, "is not a leap year"
        else:
            return a_year ,"is a leap year"
    else:
        return a_year, 'is not a leap year'
print(is_leap_year(2040))

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.
def is_consecutive(a_list):
    sortedlist = sorted(a_list)
    range_list=list(range(min(list1), max(list1)+1))
    if sortedlist == range_list:
        print("list1 has consecutive numbers")
    else:
        print("list1 has non consecutive numbers")
list1 = [1,2,0,4,5]
print(is_consecutive(list1))