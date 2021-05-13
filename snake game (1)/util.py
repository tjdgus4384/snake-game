# 게임 출처 :  https://github.com/grantjenks/free-python-games/blob/master/freegames/utils.py

"""Utilities
"""
# pylint: disable=no-member

import collections
import math
import os


def floor(value, size, offset=200):
    """Floor of `value` given `size` and `offset`.
    The floor function is best understood with a diagram of the number line::
         -200  -100    0    100   200
        <--|--x--|-----|--y--|--z--|-->
    The number line shown has offset 200 denoted by the left-hand tick mark at
    -200 and size 100 denoted by the tick marks at -100, 0, 100, and 200. The
    floor of a value is the left-hand tick mark of the range where it lies. So
    for the points show above: ``floor(x)`` is -200, ``floor(y)`` is 0, and
    ``floor(z)`` is 100.
    >>> floor(10, 100)
    0.0
    >>> floor(120, 100)
    100.0
    >>> floor(-10, 100)
    -100.0
    >>> floor(-150, 100)
    -200.0
    >>> floor(50, 167)
    -33.0
    """
    return float(((value + offset) // size) * size - offset)


def path(filename):
    "Return full path to `filename` in freegames module."
    filepath = os.path.realpath(__file__)
    dirpath = os.path.dirname(filepath)
    fullpath = os.path.join(dirpath, filename)
    return fullpath


def line(a, b, x, y):
    "Draw line from `(a, b)` to `(x, y)`."
    import turtle
    turtle.up()
    turtle.color('red')
    turtle.pensize(3)
    turtle.goto(a, b)
    turtle.down()
    turtle.goto(x, y)
    turtle.pensize(1)


def circle(x, y, size, name):
    import turtle
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.dot(size, name)

def rectangle(x, y, a, b, name):
    import turtle
    turtle.up()
    turtle.goto(x, y)
    turtle.color(name)
    turtle.down()
    turtle.begin_fill()
    for count in range(2):
       turtle.forward(a)
       turtle.left(90)
       turtle.forward(b)
       turtle.left(90)
    turtle.end_fill()

def square(x, y, size, name):
    import turtle
    turtle.up()
    turtle.goto(x, y)
    turtle.color(name)
    turtle.down()
    turtle.begin_fill()
    for count in range(4):
       turtle.forward(size)
       turtle.left(90)
    turtle.end_fill()

def squarenum(x, y, size, name, num):
    import turtle
    turtle.up()
    turtle.goto(x, y)
    turtle.color(name)
    turtle.down()
    for count in range(4):
       turtle.forward(size)
       turtle.left(90)
    turtle.up()
    turtle.goto(x, y-8)
    turtle.down()
    turtle.color("black")
    turtle.write("%d" %num, font=("Arial", 16, "normal"))

def triangle(x, y, size, name):
    import turtle
    turtle.up()
    turtle.goto(x, y)
    turtle.color(name)
    turtle.down()
    turtle.begin_fill()
    for count in range(3):
       turtle.forward(size)
       turtle.left(120)
    turtle.end_fill()


class vector(collections.Sequence):
    """Two-dimensional vector.
    Vectors can be modified in-place.
    >>> v = vector(0, 1)
    >>> v.move(1)
    >>> v
    vector(1, 2)
    >>> v.rotate(90)
    >>> v
    vector(-2.0, 1.0)
    """
    # pylint: disable=invalid-name
    PRECISION = 6

    __slots__ = ('_x', '_y', '_hash')

    def __init__(self, x, y):
        """Initialize vector with coordinates: x, y.
        >>> v = vector(1, 2)
        >>> v.x
        1
        >>> v.y
        2
        """
        self._hash = None
        self._x = round(x, self.PRECISION)
        self._y = round(y, self.PRECISION)

    @property
    def x(self):
        """X-axis component of vector.
        >>> v = vector(1, 2)
        >>> v.x
        1
        >>> v.x = 3
        >>> v.x
        3
        """
        return self._x

    @x.setter
    def x(self, value):
        if self._hash is not None:
            raise ValueError('cannot set x after hashing')
        self._x = round(value, self.PRECISION)

    @property
    def y(self):
        """Y-axis component of vector.
        >>> v = vector(1, 2)
        >>> v.y
        2
        >>> v.y = 5
        >>> v.y
        5
        """
        return self._y

    @y.setter
    def y(self, value):
        if self._hash is not None:
            raise ValueError('cannot set y after hashing')
        self._y = round(value, self.PRECISION)

    def __hash__(self):
        """v.__hash__() -> hash(v)
        >>> v = vector(1, 2)
        >>> h = hash(v)
        >>> v.x = 2
        Traceback (most recent call last):
            ...
        ValueError: cannot set x after hashing
        """
        if self._hash is None:
            pair = (self.x, self.y)
            self._hash = hash(pair)
        return self._hash

    def __len__(self):
        """v.__len__() -> len(v)
        >>> v = vector(1, 2)
        >>> len(v)
        2
        """
        return 2

    def __getitem__(self, index):
        """v.__getitem__(v, i) -> v[i]
        >>> v = vector(3, 4)
        >>> v[0]
        3
        >>> v[1]
        4
        >>> v[2]
        Traceback (most recent call last):
            ...
        IndexError
        """
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise IndexError

    def copy(self):
        """Return copy of vector.
        >>> v = vector(1, 2)
        >>> w = v.copy()
        >>> v is w
        False
        """
        type_self = type(self)
        return type_self(self.x, self.y)

    def __eq__(self, other):
        """v.__eq__(w) -> v == w
        >>> v = vector(1, 2)
        >>> w = vector(1, 2)
        >>> v == w
        True
        """
        if isinstance(other, vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __ne__(self, other):
        """v.__ne__(w) -> v != w
        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v != w
        True
        """
        if isinstance(other, vector):
            return self.x != other.x or self.y != other.y
        return NotImplemented

    def __iadd__(self, other):
        """v.__iadd__(w) -> v += w
        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v += w
        >>> v
        vector(4, 6)
        >>> v += 1
        >>> v
        vector(5, 7)
        """
        if self._hash is not None:
            raise ValueError('cannot add vector after hashing')
        if isinstance(other, vector):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return self

    def __add__(self, other):
        """v.__add__(w) -> v + w
        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v + w
        vector(4, 6)
        >>> v + 1
        vector(2, 3)
        >>> 2.0 + v
        vector(3.0, 4.0)
        """
        copy = self.copy()
        return copy.__iadd__(other)

    __radd__ = __add__

    def move(self, other):
        """Move vector by other (in-place).
        >>> v = vector(1, 2)
        >>> w = vector(3, 4)
        >>> v.move(w)
        >>> v
        vector(4, 6)
        >>> v.move(3)
        >>> v
        vector(7, 9)
        """
        self.__iadd__(other)
