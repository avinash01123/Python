# n =int(input("Enter the value of n"))
# i = 1
# mul = 1
# while(i<=n):
#     mul = mul*i
#     i= i+1
# print("Multipile of first {} number is {}".format(n, mul))


# # For Loop
# n=int(input("Enter your number"))
# sum = 0
# for i in range(n+1):
#     sum = sum +i
# print("Sum of first {} natural number is {}".format(n, sum))

# for i in range(1,4):
#     for j in range(i):
#         print(i, end='')
#     print()


# n = int(input("Enter your number:"))
# sum =0
# for i in range(n):
#     x = int(input(f"Enter Num {i}::"))
#     if(x<0):
#         continue
#     else:
#         sum = sum +x

# print(f"Sum of positive numbers you have enter is {sum}")


# n = int(input("Enter your number:"))
# sum =0
# for i in range(n):
#     x = int(input(f"Enter Num {i}::"))
#     if(x<0):
#         break
#     else:
#         sum = sum +x

# print(f"Sum of positive numbers you have enter is {sum}")

# n = int(input("Enter your number:"))
# sum =0
# for i in range(n):
#     x = int(input(f"Enter Num {i}::"))
#     if(x<0):
#         pass
#     else:
#         sum = sum +x

# print(f"Sum of positive numbers you have enter is {sum}")


# n = int(input("Enter your number:"))
# sum = 0
# for i in range(n):
#     x = int(input(f"Enter Num {i}::"))
#     if (x < 0):
#         continue
#     else:
#         sum = sum + x
# else:
#     print("Else is executed")
# print(f"Sum of positive numbers you have enter is {sum}")


n = int(input("Enter your number:"))

i=sum = 0
while(i<n):
    x = int(input(f"Enter Num {i}::"))
    if (x < 0):
        continue
    else:
        sum = sum + x
    i=i+1
else:
    print("Else is executed")
print(f"Sum of positive numbers you have enter is {sum}")