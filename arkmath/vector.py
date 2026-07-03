import math

class Vector:
    def __init__(self, components):
        self.components = components

    def __repr__(self):
        return str(self.components)

    def __add__(self, other):
        result = []
        for i in range(len(self.components)):
            result.append(self.components[i] + other.components[i])

        return Vector(result)

    def dot(self, other):
        if len(self.components) != len(other.components):
            print("Error: Vectors must be of the same length to compute dot product.") #loopy bullshit incoming
        dot = 0
        for i in range(len(self.components)):
            dot += self.components[i] * other.components[i]
        return dot

    def __mul__ (self, scalar):
        result = []
        for i in range(len(self.components)):
            result.append(self.components[i] * scalar)
        return Vector(result)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def magnitude(self):
        total = 0
        for i in range(len(self.components)):
            total += self.components[i] ** 2
        return math.sqrt(total)

    def normalise(self):
        mag = self.magnitude
        if mag == 0:
            raise ValueError("Cannot normalise zero vector")
        result = []
        for i in range(len(self.components)):
            result.append(self.components[i] / mag)
        return Vector(result)

    def cosine_similarity(self,other):
        dot_product = self.dot(other)
        magnitude_self = self.magnitude()
        magnitude_other = other.magnitude()
        if magnitude_self == 0 or magnitude_other == 0:
            raise ValueError("Cannot compute cosine similarity with zero vector")
        return dot_product/(magnitude_self * magnitude_other)
    
class Matrix:
    def __init__(self, rows):
        self.rows = rows
    def __matmul__ (self, vector):
        if len(self.rows[0]) != len(vector.components):
            raise ValueError("Matrix columns must match vector size for multiplication.")
        result = []
        for row in self.rows:
            dot_product = sum(row[i] * vector.components[i] for i in range(len(row)))
            result.append(dot_product)
        return Vector(result)

u = Vector([1,2])
v = Vector([1,2,3])
w = Vector([4,5,6])
A = Matrix([[1,2],[3,4],[5,6]])

print(A @ u)  # Matrix-vector multiplications
