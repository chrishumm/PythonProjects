def divideNo(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError: #In-build error catching
        print("Error! Do not divide by zero")

print(divideNo(10))
print(divideNo(32))
print(divideNo(3))
print(divideNo(2))
print(divideNo(0))

#Try ... except code blocks execute code up until an exception has been made

