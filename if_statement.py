# a = int(input("Enter a number"))
# print(a)


# if a == 0:
#     print(a)
# elif a > 0:
#     print("Given number is positive")
# else:
#     print("Given number is negative")

# a = int(input("Enter a number"))
# b = int(input("Enter a number"))
# c = int(input("Enter a number"))

# if a < b:
#     if a < c:
#         print("a is small")
# elif b < c:
#     print("b is small")
# else:
#     print("c is small")


a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = input("Enter an operator")


match c:
    case '+':
        print("add", a + b)
    case '-':
        print("add", a - b)
