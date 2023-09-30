
class Vector:
    def __init__(self, values):
        if isinstance(values,list):
            if Vector.is_list(values):
                self.values = values
            else:
                raise ValueError("Wrong vector type.")
        elif isinstance(values, int):
            if values < 0:
                raise ValueError("Wrong vector type.")
            self.values = []
            for i in range(values):
                self.values.append([float(i),])
        elif isinstance(values,tuple):
            if Vector.is_tuple(values):
                self.values = []
                for i in range(values[0], values[1]):
                    self.values.append([float(i),])
        else:
            raise ValueError("Wrong vector type.")
        self.shape = (len(self.values), len(self.values[0]))
        if not Vector.is_valid_shape(self.shape):
            raise ValueError("Invalid vector shape.")
        
    
    @staticmethod
    def is_list(values):
        if isinstance(values[0], list) and len(values) > 0  \
            and len(values[0]) > 0 and all(isinstance(item, (list, float)) for item in values):
            return True
        return False
    
    @staticmethod
    def is_tuple(values):
        if len(values) == 2:
            a, b = values
            if not isinstance(a, int) or not isinstance(b, int) or a >= b:
                raise ValueError("Invalid range")
            return True
        return False

    @staticmethod
    def is_valid_shape(shape):
        if (shape[0] == 1 and shape[1] > 0 or shape[0] > 0 and shape[1] == 1):
            return True
        return False


    def dot(self, other):
        if not isinstance(other, Vector) and self.shape != other.shape:
            raise ValueError("Wrong vector type.")
        else:
            res = 0
            tuple_pairs = zip(self.values, other.values)
            for el1, el2 in tuple_pairs:
                pairs = zip(el1, el2)
                for x, y in pairs:
                    res += x * y
            return res
            
    def T(self):
            new_col = []
            if self.shape[0] == 1:
                for el in self.values[0]:
                    new_col.append([el])
            else:
                col = []
                for el in self.values:
                    col.append(el[0])
                new_col.append(col)
            return Vector(new_col)
                
    def __add__(self, other):
        """Vector addition."""
        if not isinstance(other, Vector) and self.shape != other.shape:
            raise ValueError("Wrong vector type.")
        else:
            res = []
            tuple_pairs = zip(self.values, other.values)
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
            raise ValueError("Wrong vector type.")
        else:
            res = []
            tuple_pairs = zip(self.values, other.values)
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
        if not isinstance(scalar, (int, float)):
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
            raise ZeroDivisionError('division by zero')
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