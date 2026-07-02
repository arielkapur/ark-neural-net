

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