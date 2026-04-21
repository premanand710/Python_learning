
# Defult parameter and named parameter..

def register_entry(name,year,is_sudent="Yes"):
    if is_sudent=="Yes":
        ret_string = f"student name is {name} and studying year is {year}"
    else:
        ret_string = f"staff name is {name} and studying year is {year}"
    return ret_string

print(register_entry('Prem',3)) # is_sudent will become as Yes by default
print(register_entry('Kumar',2,"no")) # overwriting with no to defulat parameter is_sudent
print(register_entry(year=4,name='Kumar',is_sudent="no")) # Named parameter

# User defined function that returns value
def is_leap_year(year1):
    func_ret = False
    if (year1 % 400 == 0) and (year1 % 100 == 0):
        func_ret = True
    elif (year1 % 4 ==0) and (year1 % 100 != 0):
        func_ret = False
    
    return func_ret

year_leap = int(input("Enter an year: "))

if is_leap_year(year_leap) == True:
    print(f'{year_leap} is leap year')
else:
    print(f'{year_leap} is not leap year')


# User defined function without returns, simply executing statements, still returns None by default
def num_calculation(n1,n2): # functon definition
    num_fun = n1 + n2
    num_fun = num_fun * n1
    num_fun = num_fun + (3*n2)
    print(f"{n1} + {n2} = {num_fun}")


a = 10
b = 7
c = 6
d = 5
e = 4
f = 7

# num1 = a + b
# num1 = num1 * a
# num1 = num1 + (3*b)
# print(f"{a} + {b} = {num1}")

num_calculation(a,b) # user defined function calling
num_calculation(c,d)
retult1 = num_calculation(e,f)

print(retult1) # inbuilt function calling (print function))
