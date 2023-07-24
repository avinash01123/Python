def is_multiple_of_5(number):
    if number % 5 == 0:
        return True
    else:
        return False

num = 25
if is_multiple_of_5(num):
    print(num, "is a multiple of 5.")
else:
    print(num, "is not a multiple of 5.")
