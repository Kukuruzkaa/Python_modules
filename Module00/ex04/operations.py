import sys
import string 

def sum(x, y):
    return x + y

def difference(x, y):
    return x - y

def product(x, y):
    return x * y

def quotient(x, y):
       return x / y

def reminder(x, y):
       return  x % y

def operations(A, B):
    try:
        x = int(A)
        y = int(B)
        print("Sum:        {}".format(str(sum(x,y))))
        print("Difference: {}".format(str(difference(x,y))))
        print("Product:    {}".format(str(product(x,y))))
        try:
            num = quotient(x,y)
            formatted_number = "{:.4f}".format(num)
            if len(formatted_number) < len(str(num)):
                print("Quotient:   {}".format(str(formatted_number) + "..."))
            else:
                print("Quotient:  ", str(num))
        except ZeroDivisionError:
            print("Quotient:   ERROR (division by zero)")
        try:
            print("Reminder:   {}".format(str(reminder(x,y))))
        except ZeroDivisionError:
            print("Reminder:   ERROR (modulo by zero)")
    except ValueError:
        print("AssertionError: only integers")

def main():
    if (len(sys.argv) == 1):
        pass
    elif (len(sys.argv) == 2):
        print("AssertionError: not enough arguments provided")
    elif (len(sys.argv) != 3):
        print("AssertionError: too many arguments")
    else:
        operations(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()