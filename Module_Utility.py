def is_leap_year(year1):
    func_ret = False
    if (year1 % 400 == 0) and (year1 % 100 == 0):
        func_ret = True
    elif (year1 % 4 ==0) and (year1 % 100 != 0):
        func_ret = True
    return func_ret