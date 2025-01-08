#Last Name: Samandar
#First Name: Ahmad Naween
#Student ID: 300446112
#File: Assignment 6 part 2 (both parts)

class Point:
    '''Class that represents a point in the plane'''

    # This method initializes the point with given x and y coordinates, defaulting to (0, 0).
    def __init__(self, xcoord=0, ycoord=0):
        '''(Point, number, number) -> None
        Initializes the point to (xcoord, ycoord).'''
        self.x = xcoord
        self.y = ycoord
    # This method moves the point by the given horizontal (dx) and vertical (dy) displacements.
    def move(self, dx, dy):
        '''(Point, number, number) -> None
        Moves the point by dx and dy.'''
        self.x += dx
        self.y += dy

    # This method returns a string that represents the point in the canonical format 'Point(x, y)'.
    def __repr__(self):
        '''(Point) -> str
        Returns canonical string representation of the point.'''
        return f"Point({self.x},{self.y})"
    
    # This method checks if two points have the same coordinates.
    def __eq__(self, other):
        '''(Point, Point) -> bool
        Returns True if the points have the same coordinates.'''
        return self.x == other.x and self.y == other.y


class Rectangle:
    '''Class that represents a rectangle in a 2D plane.'''

    # This method initializes the rectangle using two Point objects for the bottom-left and top-right corners, and a color string.
    def __init__(self, bottom_left, top_right, color):
        '''(Rectangle, Point, Point, str) -> None
        Initializes the rectangle with its bottom-left and top-right corners, and color.'''
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.color = color

    # This method returns the bottom-left corner of the rectangle.
    def get_bottom_left(self):
        '''(Rectangle) -> Point
        Returns the bottom-left corner of the rectangle.'''
        return self.bottom_left

    # This method returns the top-right corner of the rectangle.
    def get_top_right(self):
        '''(Rectangle) -> Point
        Returns the top-right corner of the rectangle.'''
        return self.top_right

    # This method returns the color of the rectangle.
    def get_color(self):
        '''(Rectangle) -> str
        Returns the color of the rectangle.'''
        return self.color

    # This method changes the rectangle's color to a new color.
    def reset_color(self, new_color):
        '''(Rectangle, str) -> None
        Changes the rectangle's color to new_color.'''
        self.color = new_color

    # This method calculates and returns the perimeter of the rectangle.
    def get_perimeter(self):
        '''(Rectangle) -> number
        Returns the perimeter of the rectangle.'''
        width = self.top_right.x - self.bottom_left.x
        height = self.top_right.y - self.bottom_left.y
        return 2 * (width + height)

    # This method calculates and returns the area of the rectangle.
    def get_area(self):
        '''(Rectangle) -> number
        Returns the area of the rectangle.'''
        width = self.top_right.x - self.bottom_left.x
        height = self.top_right.y - self.bottom_left.y
        return width * height

    # This method moves the entire rectangle by the given horizontal (dx) and vertical (dy) displacements.
    def move(self, dx, dy):
        '''(Rectangle, number, number) -> None
        Moves the rectangle by dx and dy.'''
        self.bottom_left.move(dx, dy)
        self.top_right.move(dx, dy)

    # This method checks if the rectangle intersects with another rectangle.
    def intersects(self, other):
        '''(Rectangle, Rectangle) -> bool
        Returns True if the rectangle intersects with another rectangle.'''
        return not (self.top_right.x <= other.bottom_left.x or
                    self.bottom_left.x >= other.top_right.x or
                    self.top_right.y <= other.bottom_left.y or
                    self.bottom_left.y >= other.top_right.y)

    # This method checks if a given point (x, y) is inside the rectangle.
    def contains(self, x, y):
        '''(Rectangle, number, number) -> bool
        Returns True if the point (x, y) is inside the rectangle.'''
        return (self.bottom_left.x <= x <= self.top_right.x and
                self.bottom_left.y <= y <= self.top_right.y)
    
    # This method returns a string that represents the rectangle in the canonical format 'Rectangle(bottom_left, top_right, color)'.
    def __repr__(self):
        '''(Rectangle) -> str
        Returns canonical string representation of the rectangle.'''
        return f"Rectangle({repr(self.bottom_left)},{repr(self.top_right)},'{self.color}')"

    # This method returns a user-friendly string representation of the rectangle.
    def __str__(self):
        '''(Rectangle) -> str
        Returns a user-friendly string representation of the rectangle.'''
        return (f"I am a {self.color} rectangle with bottom left corner at "
                f"({self.bottom_left.x}, {self.bottom_left.y}) and top right corner at "
                f"({self.top_right.x}, {self.top_right.y}).")

    # This method checks if two rectangles are identical based on their bottom-left corner, top-right corner, and color.
    def __eq__(self, other):
        '''(Rectangle, Rectangle) -> bool
        Returns True if the rectangles are identical.'''
        return (self.bottom_left == other.bottom_left and
                self.top_right == other.top_right and
                self.color == other.color)


class Canvas:
    '''Class that represents a collection of rectangles.'''

    # This method initializes the canvas with an empty list of rectangles.
    def __init__(self):
        '''(Canvas) -> None
        Initializes an empty canvas.'''
        self.rectangles = []

    # This method returns the number of rectangles in the canvas.
    def __len__(self):
        '''(Canvas) -> int
        Returns the number of rectangles in the canvas.'''
        return len(self.rectangles)

    # This method adds a rectangle to the canvas.
    def add_one_rectangle(self, rectangle):
        '''(Canvas, Rectangle) -> None
        Adds a rectangle to the canvas.'''
        self.rectangles.append(rectangle)

    # This method counts and returns the number of rectangles in the canvas that have the given color.
    def count_same_color(self, color):
        '''(Canvas, str) -> int
        Returns the number of rectangles of the given color.'''
        return sum(1 for rect in self.rectangles if rect.color == color)

    # This method calculates and returns the sum of the perimeters of all rectangles in the canvas.
    def total_perimeter(self):
        '''(Canvas) -> number
        Returns the sum of the perimeters of all rectangles.'''
        return sum(rect.get_perimeter() for rect in self.rectangles)

    # This method returns the smallest rectangle that encloses all rectangles on the canvas.
    def min_enclosing_rectangle(self):
        '''(Canvas) -> Rectangle
        Returns the smallest rectangle that encloses all rectangles in the canvas.'''
        if not self.rectangles:
            return None
        min_x = min(rect.bottom_left.x for rect in self.rectangles)
        min_y = min(rect.bottom_left.y for rect in self.rectangles)
        max_x = max(rect.top_right.x for rect in self.rectangles)
        max_y = max(rect.top_right.y for rect in self.rectangles)
        return Rectangle(Point(min_x, min_y), Point(max_x, max_y), 'red')

    # This method checks if there is a common point among all rectangles in the canvas.
    def common_point(self):
        '''(Canvas) -> bool
        Returns True if there is a common point among all rectangles.'''
        if not self.rectangles:
            return False
        intersect = self.rectangles[0]
        for rect in self.rectangles[1:]:
            if not intersect.intersects(rect):
                return False
            intersect = Rectangle(
                Point(max(intersect.bottom_left.x, rect.bottom_left.x),
                      max(intersect.bottom_left.y, rect.bottom_left.y)),
                Point(min(intersect.top_right.x, rect.top_right.x),
                      min(intersect.top_right.y, rect.top_right.y)),
                ''
            )
        return True
    
    # This method returns a string that represents the canvas in the canonical format 'Canvas(rectangles)'.
    def __repr__(self):
        '''(Canvas) -> str
        Returns canonical string representation of the canvas.'''
        return f"Canvas({self.rectangles})"

print("")
print("Rectangle and Point Classes")
print("")
# Testing Rectangle and Point Classes
r1 = Rectangle(Point(), Point(1, 1), "red")
print(r1)
print(r1.get_color())
print(r1.get_bottom_left())
print(r1.get_top_right())
r1.reset_color("blue")
print(r1.get_color())
print(r1)
r1.move(2, 3)
print(r1)
print(r1.__str__())

r2 = eval(repr(r1))
print(r2)
print(r1 is r2)
print(r1 == r2)

r3 = Rectangle(Point(), Point(2, 1), "red")
print(r3.get_perimeter())
r4 = Rectangle(Point(1, 1), Point(2, 2.5), "blue")
print(r4.get_area())
r5 = Rectangle(Point(1, 1), Point(2, 2.5), "blue")
print(r4 == r5)
print(r4 is r5)

r6 = Rectangle(Point(1, 1), Point(2, 2.5), "red")
print(r5 == r6)

r = Rectangle(Point(1, 1), Point(2, 5), "blue")
print(r.contains(1.5, 1))
print(r.contains(2, 2))
print(r.contains(0, 0))

print("")
print("The intersection")
print("")

# Testing Intersections
r1 = Rectangle(Point(1, 1), Point(2, 2), "blue")
r2 = Rectangle(Point(2, 2.5), Point(3, 3), "blue")
r3 = Rectangle(Point(1.5, 0), Point(1.7, 3), "red")
print(r3)
print(r1.intersects(r2))
print(r2.intersects(r1))
print(r1.intersects(r3))
print(r2.intersects(r3))

print("")
print("The Canvas Class")
print("")

# Testing Canvas Class
c = Canvas()
print(len(c))
r1 = Rectangle(Point(1, 1), Point(2, 2), "blue")
r2 = Rectangle(Point(2, 2.5), Point(3, 3), "blue")
r3 = Rectangle(Point(1.5, 0), Point(1.7, 3), "red")
c.add_one_rectangle(r1)
c.add_one_rectangle(r2)
c.add_one_rectangle(r3)
c.add_one_rectangle(Rectangle(Point(0, 0), Point(100, 100), "orange"))
print(len(c))
print(c)
print(c.count_same_color("blue"))
print(c.count_same_color("red"))
print(c.count_same_color("purple"))

c = Canvas()
r1 = Rectangle(Point(1, 1), Point(2, 2), "blue")
r2 = Rectangle(Point(1, 1), Point(4, 4), "blue")
r3 = Rectangle(Point(-2, -2), Point(-1, -1), "blue")
c.add_one_rectangle(r1)
c.add_one_rectangle(r2)
c.add_one_rectangle(r3)
print(c.total_perimeter())

c = Canvas()
r1 = Rectangle(Point(1, 1), Point(2, 2), "blue")
r2 = Rectangle(Point(1, 1), Point(4, 4), "blue")
r3 = Rectangle(Point(-2, -2), Point(-1, -1), "blue")
r4 = Rectangle(Point(0, -100), Point(1, 100), "yellow")
c.add_one_rectangle(r1)
c.add_one_rectangle(r2)
c.add_one_rectangle(r3)
c.add_one_rectangle(r4)
print(c.min_enclosing_rectangle())

c = Canvas()
r1 = Rectangle(Point(1, 1), Point(2, 2), "blue")
r2 = Rectangle(Point(1.5, 1.5), Point(4, 4), "blue")
r3 = Rectangle(Point(-2, -2), Point(2, 1.5), "blue")
r4 = Rectangle(Point(0, -100), Point(1.5, 100), "yellow")
c.add_one_rectangle(r1)
c.add_one_rectangle(r2)
c.add_one_rectangle(r3)
c.add_one_rectangle(r4)
print(c.common_point())

c = Canvas()
r1 = Rectangle(Point(-2, -2), Point(-1, 2), "blue")
r2 = Rectangle(Point(-2, -2), Point(2, -1), "blue")
r3 = Rectangle(Point(1, -2), Point(2, 2), "blue")
r4 = Rectangle(Point(-2, 1), Point(2, 2), "blue")
c.add_one_rectangle(r1)
c.add_one_rectangle(r2)
c.add_one_rectangle(r3)
c.add_one_rectangle(r4)
print(c.common_point())
