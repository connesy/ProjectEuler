# -*- coding: utf-8 -*-
"""
@author: Stefan Mejlgaard
"""

import math
from collections import Counter, namedtuple


class Triangle(namedtuple("Triangle", ["a", "b"])):
    __slots__ = ()

    @property
    def c(self) -> float:
        return (self.a**2 + self.b**2) ** 0.5

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    def __str__(self) -> str:
        return f"Triangle: a={self.a:3d}  b={self.b:3d}  c={self.c:7.3f}  p={self.perimeter:8.3f}"

    __repr__ = __str__

    def is_integral(self) -> bool:
        c = self.c
        return math.isclose(c, int(c), abs_tol=1e-8)


def integer_triangles(max_perimeter: int = 1000) -> list[Triangle]:
    """Create a list containing all possible right-angle triangles with maximum perimeter `max_perimeter`, where
    a, b and c are all integers"""

    triangles: list[Triangle] = []

    # Since the perimeter p >= 2b, we can limit b to be p/2
    for b in range(1, max_perimeter // 2):
        # Although not explicitly specified in the problem, the solutions given limit a <= b
        for a in range(1, b + 1):
            triangle = Triangle(a, b)
            if not triangle.is_integral():
                continue

            if triangle.perimeter > max_perimeter:
                continue

            triangles.append(triangle)

    return triangles


if __name__ == "__main__":
    triangles = integer_triangles(max_perimeter=1000)

    most_common_perimeters = Counter(t.perimeter for t in triangles).most_common()
    print(*most_common_perimeters[:5], sep="\n")
