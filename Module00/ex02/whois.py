import sys

if len(sys.argv) > 1:
    try:
        if len(sys.argv) > 2:
            print("Error: more than one argument are provided")
        else:
            num = int(sys.argv[1])
            if num == 0:
                print("I'm Zero")
            elif (num % 2) == 0:
                print("I'm Even")
            else:
                print("I'm Odd")
    except:
        print("Error: argument is not an integer")
    
    # except ValueError as exc:
    # print(exc)