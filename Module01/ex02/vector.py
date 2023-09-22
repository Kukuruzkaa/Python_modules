
class Vector:
    def __init__(self, values):
        if Vector.is_list(values):
            self.values = values
        elif isinstance(values, int):
            if values < 0:
                raise ValueError
            self.values = []
            for i in range(values):
                self.values.append([float[i],])
        elif Vector.is_tuple(values):
            self.values = []
            for i in range(values[0], values[1]):
                self.values.append([float[i],])
        else:
            raise ValueError
        self.shape = (len(self.values), len(self.values[0]))
        if not Vector.is_valid_shape(self.shape):
            raise ValueError
        
    
    @staticmethod
    def is_list(values):
        if len(values) > 0 and isinstance(values, list) \
            and len(values[0]) > 0 and all(isinstance(item, (list, float)) for item in values):
            return True
        return False
    
    @staticmethod
    def is_tuple(values):
        if len(values) == 2:
            a, b = values
            if not isinstance(a, int) or not isinstance(b, int) or a < b:
                raise ValueError("Invalid range")
            return True
        return False

    @staticmethod
    def is_valid_shape(shape):
        if (shape[0] == 1 and shape[1] > 0 or shape[0] > 0 and shape[1] == 1):
            return True
        return False


    def dot(self, other):
        if not isinstance(other, Vector) and self.shape == other.shape:
            raise ValueError("Wrong vector types.")
        else:
            res = 0
            tuple_pairs = zip(self, other)
            for el1, el2 in tuple_pairs:
                pairs = zip(el1, el2)
                for x, y in pairs:
                    res += x * y
                    return res
                
    def __add__(self, other):
        """Vector addition."""
        if not isinstance(other, Vector) and self.shape == other.shape:
            raise ValueError("Wrong vector types.")
        else:
            res = []
            tuple_pairs = zip(self, other)
            for el1, el2 in tuple_pairs:
                pairs = zip(el1, el2)
                new_list = [x + y for x, y in pairs]
                res.append(new_list)
            return Vector(res)
        
    def __radd__(self, other):
        """Vector addition."""
        return self.__add__(other)
        
    def __sub__(self, other):
        """Vector subtraction."""
        if not isinstance(other, Vector) and self.shape == other.shape:
            raise ValueError("Wrong vector types.")
        else:
            res = []
            tuple_pairs = zip(self, other)
            for el1, el2 in tuple_pairs:
                pairs = zip(el1, el2)
                new_list = [x - y for x, y in pairs]
                res.append(new_list)
            return Vector(res)
    
    def __rsub__(self, other):
        """Vector subtraction."""
        return self.__sub__(other)
    
    def __str__(self):
        return str(self.values)  
                    
    def __mul__(self, scalar):
        """Multiplication of a vector by a scalar."""
        if not isinstance(scalar, int) or isinstance(scalar, float):
            raise ValueError('Can only multiply Vector by a scalar')  
        else:
            res = []
            for col in self.values:
                new_col = []
                for el in col:
                    new_el = el * scalar
                    new_col.append(new_el)
                res.append(new_col)
            return Vector(res)
    
    def __rmul__(self, scalar):
        """Multiplication of a vector by a scalar."""
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        """True division of the vector by a scalar.""" 
        if not isinstance(scalar, (int, float)):
            raise ValueError('Can only devide Vector by a scalar')
        if scalar == 0:
            raise ZeroDivisionError
        else:
            res = []
            for col in self.values:
                new_col = []
                for el in col:
                    new_el = el / scalar
                    new_col.append(new_el)
                res.append(new_col)
            return Vector(res)
    
    def __rtruediv__(self, scalar):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")
            
    def __repr__(self):
        """Unambiguous string representation of the vector."""
        return self.__str__(self)

    def T(self):
        if self.shape == 1:
            new_col = []
            for el in self.values[0]:
                new_col.append([el])
            return Vector(new_col)
                
                
                
    

