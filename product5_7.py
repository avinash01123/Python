def is_multiple_of_5_and_7(number):
    if number % 5 == 0 and number % 7 == 0:
        return True
    else:
        return False

num = 35
if is_multiple_of_5_and_7(num):
    print(num, "is a multiple of both 5 and 7.")
else:
    print(num, "is not a multiple of both 5 and 7.")