# Decorators in Python


#Assigning Functions to Variables
def plus_one(number):
    return number + 1

add_one = plus_one
add_one(5)




#Defining Functions Inside other Functions
def add_one(num):
    def add_two(num):
        return num+1
    result=add_two(num)
    return result

add_one(4)





#Passing Functions as Arguments to other Functions

def add_onee(number):
    return number+1

def fun_call(function):
    num_to_add=5
    return function(num_to_add)

fun_call(add_onee)

#Functions Returning other Functions

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
hello()




# Creating Decorators

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_upper=func.upper()
        return make_upper
    return wrapper

def say_hello():
    return "namaskar"

decorate=uppercase_decorator(say_hello)

decorate()

# NAMASKAR



#Python provides a much easier way for us to apply decorators. 
#We simply use the @ symbol before the function we'd like to decorate
@uppercase_decorator
def say_hello_DECOR():
    return "namaskar"

say_hello_DECOR()

# NAMASKAR




#Applying Multiple Decorators to a Single Function
def split_str(function):
    def wrapp():
        fun=function()
        splitted=fun.split()
        return splitted
    return wrapp

@uppercase_decorator
@split_str
def say_hello_multi_decor():
    return "namaskar shubhprabhat"

say_hello_multi_decor()




#Accepting Arguments in Decorator Functions
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities are {0} and {1}".format(city_one, city_two))

cities("Solapur", "Pune")




#Defining General Purpose Decorators
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()
 #We use the name kwargs(Keyword Arguments) with the double star. 
 #The reason is because the double star allows us to pass through keyword arguments
 #kwargs is a dictionary of keyword arguments. The ** allows us to pass any number of keyword arguments. 
 #A keyword argument is basically a dictionary. 





 #Passing Arguments to the Decorator
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")




#Debugging Decorators
#Python provides a functools.wraps decorator. 
#This decorator copies the lost metadata from the undecorated function to the decorated closure
import functools

def uppercase_decorator2(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_decorator2
def say_hi2():
    "This will say hi"
    return 'hello there'

say_hi2()    

#It is advisable and good practice to always use functools.wraps when defining decorators.
#It will save you a lot of headache in debugging.























# Decorators dynamically alter the functionality of a function, method, or class without having to directly use subclasses or change the source code of the function being decorated. 
# Using decorators in Python also ensures that your code is DRY(Don't Repeat Yourself). Decorators have several use cases such as:

#     Authorization in Python frameworks such as Flask and Django
#     Logging
#     Measuring execution time
#     Synchronization





















