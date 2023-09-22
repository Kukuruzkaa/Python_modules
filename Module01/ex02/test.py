from vector import Vector

if __name__ == "__main__":
    
    # Column vector of shape n * 1
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = v1 * 5
    print(v2)
    # Expected output:
    # Vector([[0.0], [5.0], [10.0], [15.0]])
    # Row vector of shape 1 * n
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = v1 * 5
    print(v2)
    # Expected output
    # Vector([[0.0, 5.0, 10.0, 15.0]])
    v2 = v1 / 2.0
    print(v2)

    # Expected output
    # Vector([[0.0], [0.5], [1.0], [1.5]])
    v1 / 0.0
    # Expected ouput
    # ZeroDivisionError: division by zero.
    # 2.0 / v1
    # Expected output:
    # NotImplementedError: Division of a scalar by a Vector is not defined here.

    # values = [[1.0, 2.0], [3.0, 4.0]]
    # is_list = Vector.is_list(values)
    # print(is_list)  # Should print True if values is a valid list

    # # Or if it's not in a class, just call it directly
    # values = [[1.0, 2.0], [3.0, 4.0]]
    # is_list = is_list(values)
    # print(is_list) 
    # # Should also print True if values is a valid list