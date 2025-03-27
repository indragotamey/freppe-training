
import os

''' msg = 'Hello World'
print(msg)

list_1 = list([2, 4, 'may', 'june'])
print(list_1)
touple_var = (2, 3, 5)
print(type(touple_var)) '''

'''error handling scenarios'''
''' try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Division by 0 is not allowed")
except ValueError:
    print("Enter a valid number")
else:
    print("Operation Successful")
finally:
    print("This will always execute no matter the exception") '''



'''data manupulation functions'''

''' def remove_duplicates(lst):
    return list(dict.fromkeys(lst))
print(remove_duplicates([1,2,3,2,4,1]));

def get_unique_values(lst):
    return set(lst)
list_1 = [1,1,2,3,3,4,5,5,6]
print(get_unique_values(list_1))   

def find_common_elements(lst1,lst2):
    return list(set(lst1) & set(lst2))
list1 = [1,2,3,5,7,9,11]
list2 = [0,1,2,3,5,8,13]
print(find_common_elements(list1,list2)) '''

def list_files():
    files = os.listdir()
    if not files:
        print("no files found in the directory.")
    else:
        print("\nFiles found in the current directory")
        for file in files:
            print(f" - {file}")

def read_file():
    filename = input("Enter a filename to read:")
    if os.path.exists(filename):
        with open(filename, "r", encoding = "utf-8")as file:
            print("\nFile contains:\n")
            print(file.read())
    else:
        print("Error: File not found!")


def delete_file():
    filename = input("Enter a filename to delete")
    if os.path.exists(flename):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully!")
    else:
        print("Error: File not found")

def main():
    while True:
        print("\nSimple File Manager - Command Line Tool")
        print("1. List Files")
        print("2. Read a file")
        print("3. Delete a file")
        print("4. Exit")

        choice = input("Enter your choice (1-4)")
        if choice == 1:
            list_files()
        elif choice == 2:
            read_file()
        elif choice == 3:
            delete_file()
        elif choice == 4:
            print("Exiting the program. Goodbye")
            break
        else:
            print("Invalid choice! Please enter number between 1 - 4")

if __name__ == "__main__":
    main()





