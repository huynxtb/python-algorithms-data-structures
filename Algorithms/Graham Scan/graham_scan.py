from typing import List
import functools

class Point:
    """Represents a 2D point with x and y coordinates."""
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

def dist_sq(p1: Point, p2: Point) -> float:
    """Calculates the squared Euclidean distance between two points."""
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2

def ccw(p1: Point, p2: Point, p3: Point) -> float:
    """
    Determines the orientation of the triplet (p1, p2, p3).
    Returns:
        > 0 for counter-clockwise turn
        < 0 for clockwise turn
        0 for collinear points
    """
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

def graham_scan(points: List[Point]) -> List[Point]:
    """
    Finds the convex hull of a set of 2D points using the Graham Scan algorithm.
    
    Excludes collinear points on the boundary, returning only the extreme vertices
    in counter-clockwise order.
    
    Args:
        points: A list of Point objects.
        
    Returns:
        A list of Point objects representing the vertices of the convex hull
        in counter-clockwise order.
        
    Time Complexity: O(N log N) where N is the number of input points.
    Space Complexity: O(N) to store the sorted points and the stack.
    """
    n = len(points)
    if n < 3:
        return list(points)

    p0 = min(points, key=lambda p: (p.y, p.x))

    def compare(p1: Point, p2: Point) -> int:
        order = ccw(p0, p1, p2)
        if order == 0:
            d1 = dist_sq(p0, p1)
            d2 = dist_sq(p0, p2)
            if d1 == d2:
                return 0
            return -1 if d1 < d2 else 1
        return -1 if order > 0 else 1

    remaining = [p for p in points if p is not p0]
    remaining.sort(key=functools.cmp_to_key(compare))

    filtered: List[Point] = []
    for p in remaining:
        while filtered and ccw(p0, filtered[-1], p) == 0:
            filtered.pop()
        filtered.append(p)

    if len(filtered) < 2:
        return [p0] + filtered

    stack = [p0, filtered[0], filtered[1]]
    for i in range(2, len(filtered)):
        while len(stack) > 1 and ccw(stack[-2], stack[-1], filtered[i]) <= 0:
            stack.pop()
        stack.append(filtered[i])

    return stack