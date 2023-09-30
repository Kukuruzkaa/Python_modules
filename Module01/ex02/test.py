from vector import Vector
import colorama
from colorama import Fore

if __name__ == "__main__":
    
    try:
        vector = Vector(-4)
    except ValueError:
        print(f"{Fore.RED}ValueError: wrong vector type")
    try:
        vec = Vector((1, 1))
    except ValueError:
        print(f"{Fore.RED}ValueError: invalid range - []")

    # # v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    # # v2 = v1 * 5
    # # print(v1.values)
    # # print(v2)
    # # v3 = Vector(4)
    # # print(v3)

    # # print(Vector([1. , 2e-3, 3.14, 5.]).values)
    # # print(Vector(4).values)
  
    # # print(Vector((10, 12)).values)
    # # print(Vector((3, 1)).values)
    
    # # v = Vector((1, 1))
    # # print(v.values)
    
    # # Vector((4, 7.1))
    
    # # v = Vector(4)
    # # print(v.values)
    
    # # print(v * 4)
    
    # # print(4.0 * v)
    
    # # v * "hi"
    
    # v = Vector(4)
    # print(v)
    # v2 = Vector([[1.0], [1.0], [1.0], [1.0]])
    # print(v2)
    # print((v + v2).values)
    
    # # v + Vector([0.0, 0.0, 0.0, 0.0])
    # # v + "hello"
    # # v + None
    # print((v - v2).values != (v2 - v).values)
    # Vector(4) / 2
    # Vector(4) / 3.14
    # # Vector(4) / 0
    # # Vector(4) / None
    # # None / Vector(4)
    # 3 / Vector(3)

