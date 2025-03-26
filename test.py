''' msg = 'Hello World'
print(msg)

list_1 = list([2, 4, 'may', 'june'])
print(list_1)
touple_var = (2, 3, 5)
print(type(touple_var)) '''

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Division by 0 is not allowed")
except ValueError:
    print("Enter a valid number")
else:
    print("Operation Successful")
finally:
    print("This will always execute no matter the exception")
        
