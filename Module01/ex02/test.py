from vector import Vector
import colorama
from colorama import Fore

colorama.init(autoreset=True)

if __name__ == "__main__":
    
    print(f"{Fore.BLUE}Vector creation tests: ")
    try:
        vector = Vector(-4)
    except ValueError:
        print(f"{Fore.RED}ValueError: wrong vector type")
    try:
        vct = Vector([[1], [2], [3]])
    except ValueError:
        print(f"{Fore.RED}ValueError: wrong vector type")
    try:
        vec = Vector((1, 1))
    except ValueError:
        print(f"{Fore.RED}ValueError: invalid range - []")
    try:
        vec = Vector((5, 2))
    except ValueError:
        print(f"{Fore.RED}ValueError: invalid range - [5 > 2]\n")
    
    
    print(f"{Fore.GREEN}Row vector: ")
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    print("V1 =", v1.values)
    
    print(f"{Fore.YELLOW}Column vector: ")
    v2 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print("V2 =",v2)
    print()
    
    print(f"{Fore.MAGENTA}Vector methods: \n")
    print(f"{Fore.BLUE}__mull__/__sub__:")
    v3 = v1 * 5
    print("V3 =", v3.values)
    print("V3 shape =", v3.shape)
    
    v4 = v2 * 5
    print("V4 =", v4.values)
    print("V4 shape =", v4.shape)
    
    v3 = v1 / 2
    print("V3 =", v3.values)
    v4 = v2 / 2
    print("V4 =", v4.values)
    
    v5 = Vector((5))
    print("V5 =", v5.values)
    print("V5 shape =", v5.shape)
    
    v6 = Vector((1,6))
    print("V6 =", v6.values)
    print("V6 shape =", v6.shape)
    
    try:
        v1 / 0.0
    except ZeroDivisionError:
        print(f"{Fore.RED}ZeroDivisionError: division by zero")
    try:
        2.0 / v2
    except NotImplementedError:
        print(f"{Fore.RED}NotImplementedError: Division of a scalar by a Vector is not defined here")
    try:
        v1 / v2
    except ValueError:
        print(f"{Fore.RED}ValueError: Can only devide Vector by a scalar")
    try:
        v1 / None
    except ValueError:
        print(f"{Fore.RED}ValueError: Can only devide Vector by a scalar")
    try:
        None / v2
    except NotImplementedError:
        print(f"{Fore.RED}NotImplementedError: Division of a scalar by a Vector is not defined here")
    try:
        v1 * "vector"
    except ValueError:
        print(f"{Fore.RED}ValueError: Can only multiply Vector by a scalar\n")
   
    print(f"{Fore.BLUE}.T():")
    
    print("v5.T() =", v5.T())
    print("V5 new shape =", v5.T().shape)
   
    print("v6.T() =", v6.T())
    print("V6 new shape =", v6.T().shape)
    print()

    print(f"{Fore.BLUE}.dot():")
    
    print("dot V5 & V6 =", v5.dot(v6))
    
    v7 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print("V7 =", v7)
    v8 = Vector([[2.0], [1.5], [2.25], [4.0]])
    print("V8 =", v8)
    print("dot V7 & V8 =", v7.dot(v8))
    
    try:
        print("dot V5 & V7 =", v5.dot(v7))
    except:
        print(f"{Fore.RED}ValueError: wrong vector type - dot V5 & V7 different shape")
        

 
    

    


    # v2 = Vector([[1.0], [1.0], [1.0], [1.0]])
    # print(v2)
    # print((v + v2).values)
    
    # v + Vector([0.0, 0.0, 0.0, 0.0])
    # v + "hello"
    # v + None
    # print((v - v2).values != (v2 - v).values)
  



