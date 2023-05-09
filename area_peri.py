"""importing the math function"""
import math

#from datetime import datetime, timedelta


class AreaPerimeter:
    """creating the class"""

    def __init__(self):  # creating the constructor or default constructor
        print("area,perimeter,volume")

    def circle(self):
        """ Circle method or function"""
        print('\nSelected Shape is Circle')
        radius = float(input('\nEnter the radius of Circle: '))
        u_input=int(input('select the choice for calculation\n1.area\n2.perimeter\n3.volume'))
        if u_input == 1:
            print('Area of Circle : ', round(math.pi * radius * radius, 2))
        elif u_input == 2:
            print('Perimeter of Circle : ', round(2 * math.pi * radius, 2))
        elif u_input:
            print('volume of circle:', round((4 / 3) * math.pi * radius ** 3, 2))

    def square(self):
        """method for square"""
        print('Selected Shape is Square')
        side = float(input('Enter the side of square: '))
        print('Area of Square : ', round(side ** 2, 2))
        print('Perimeter of Square : ', round(4 * side, 2))
        print('volume of square:', side ** 3)

    def rectangle(self):
        """method for rectangle"""
        print('Selected Shape is Rectangular')
        length = float(input('Enter the length of Rectangular: '))
        breadth = float(input('Enter the width of Rectangular: '))
        print('Area of Rectangular : ', round(length * breadth, 2))
        peri = round(2 * (length * breadth), 2)
        print('Perimeter of Rectangular : ', peri)
        height = round(peri / 2 - breadth)
        print('volume of the Rectangle:', round(length * breadth * height, 2))

    def triangle(self):
        """method for triangle"""
        print('Selected Shape is Triangular')
        height = float(input('Enter the height of triangle: '))
        base = float(input('Enter the Base of triangle: '))
        side_1 = float(input('Enter the Side-1 of triangle: '))
        side_2 = float(input('Enter the Side-2 of triangle: '))
        print('Area of Triangle : ', round((height * base) / (2), 2))
        if base + side_2 > side_1:
            print('Perimeter of Triangle : ', round(side_1 + base + side_2, 2))
        else:
            print('Enter valid input! Rule ')
        print('volume of Triangle:', base * height)

    def cylinder(self):
        """method"""
        print('Selected Shape is Cylinder')
        radius = float(input('Enter the radius of Cylinder: '))
        height = float(input('Enter the height of Cylinder: '))
        print('Area of Cylinder : ', round(
            (2 * math.pi * radius * height) + (2 * math.pi * radius * radius), 2))
        print('Perimeter of Cylinder : ', round(2 * (2 * radius + height), 2))
        print('Volume of Cylinder:', round(math.pi * radius ** 2 * height, 2))

    def rhombus(self):
        """method"""
        print('Selected Shape is Rhombus')
        vertical = float(input('Enter the Vertical diameter of Rhombus: '))
        horizontal = float(input('Enter the Horizontal diameter of Rhombus: '))
        side = float(input('Enter the Side of Rhombus: '))
        area = round((vertical * horizontal) / 2, 2)
        print('Area of Cylinder : ', area)
        print('Perimeter of Cylinder : ', round(4 * side, 2))
        print('Volume of Rhombus:', area * vertical)

    def cube(self):
        """method"""
        print('Selected Shape is Cube')
        edge = float(input('Enter the Edge of Cube: '))
        side_length = float(input('Enter the side length of Cube: '))
        print('Area of Cube : ', round((6 * edge * edge), 1))
        print('Perimeter of cube : ', round((12 * side_length), 1))
        print('volume of cube:', edge ** 3)

    def cuboid(self):
        """method"""
        print('Selected Shape is Cuboid')
        length = float(input('Enter the Length of the Cuboid: '))
        width = float(input('Enter the Width of the Cuboid: '))
        height = float(input('Enter the Height of the Cuboid: '))
        print('Area of Cuboid : ', round((2 * length * width) +
                                         (2 * length * height) + (2 * height * width), 2))
        print('Perimeter of Cuboid : ', round(4 * length * width * height, 2))
        print('volume of cuboid:', length * height * width)

    def pentagon(self):
        """method"""
        print('Selected Shape is Pentagon')
        side = float(input('Enter the side of Pentagon: '))
        print('Area of Pentagon : ', round(
            (1 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side * side, 2))
        print("perimeter of Pentagon : ", round(5 * side, 2))

    def hexagon(self):
        """methhod"""
        print('Selected Shape is Hexagon')
        side = float(input('Enter the side of hexagon: '))
        print('Area of hexagon : ', round(((5.196) / (2)) * (side ** 2), 2))
        print('Perimeter of hexagon : ', round(6 * side, 2))


print("""
1. Circle
2. Square
3. Rectangular
4. Triangular
5. Cylinder
6. Rhombus
7. Cube
8. Cuboid
9. pentagon
10. Hexagon""")

user_input = int(input('\nEnter the Option based on Shape: '))
obj = AreaPerimeter()
if user_input == 1:
    obj.circle()
elif user_input == 2:
    obj.square()
elif user_input == 3:
    obj.rectangle()
elif user_input == 4:
    obj.triangle()
elif user_input == 5:
    obj.cylinder()
elif user_input == 6:
    obj.rhombus()
elif user_input == 7:
    obj.cube()
elif user_input == 8:
    obj.cuboid()
elif user_input == 9:
    obj.pentagon()
elif user_input == 10:
    obj.hexagon()
else:
    print('Enter Option is Invalid')
