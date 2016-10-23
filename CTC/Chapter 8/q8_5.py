def multiply_numbers(a,b):
    if a > b:
        small = b
        big = a
    else:
        big = b
        small = a
    return multiply_helper(small,big)

def multiply_helper(small,big):
    if small == 0:
        return 0
    elif small == 1:
        return big

    s = small>>1
    side1 = multiply_numbers(s,big)
    if small%2==0:
        return 2*side1
    else:
        return 2*side1+big


#def multiply_two_numbers(small,big):
print(multiply_numbers(2,3))