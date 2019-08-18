class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        # if type(other) == 'int' or type(other) == 'float':
        return Point2(self.x * other, self.y * other)

# class Point:
#     def __init__(self, x, y, z=None):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __add__(self, other):
#         if self.z is not None:
#             return Point(self.x + other.x, self.y + other.y, self.z + other.z)
#         else:
#             return Point(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other):
#         if self.z is not None:
#             return Point(self.x - other.x, self.y - other.y, self.z - other.z)
#         else:
#             return Point(self.x - other.x, self.y - other.y)
#
#     def __mul__(self, other):
#         if type(other) == 'int':
#             if self.z is not None:
#                 return Point(self.x * other, self.y * other, self.z * other)
#             else:
#                 return Point(self.x * other, self.y * other)
#
