# Graham Scan Algorithm

## Introduction
The Graham Scan algorithm finds the convex hull of a finite set of 2D points. The convex hull is the smallest convex polygon containing all the points in the set. This algorithm is widely used in computational geometry, robotics, and pattern recognition.

## Usage

from graham_scan import Point, graham_scan

points = [
    Point(0, 3), Point(1, 1), Point(2, 2), Point(4, 4),
    Point(0, 0), Point(1, 2), Point(3, 1), Point(3, 3)
]

hull = graham_scan(points)
for p in hull:
    print(f"({p.x}, {p.y})")
# Output will be the vertices of the convex hull in counter-clockwise order.


## Detailed Explanation
1. **Find the Pivot**: Locate the point with the lowest y-coordinate ($P_0$). If there is a tie, choose the one with the lowest x-coordinate. This point is guaranteed to be on the convex hull.
2. **Sort by Polar Angle**: Sort the remaining points based on their polar angle relative to $P_0$. If two points have the same angle, sort them by distance from $P_0$ and keep only the furthest point, discarding the others.
3. **Scan**: Iterate through the sorted points while maintaining a stack of the hull vertices. For each point, check if the turn from the second-to-last point to the last point to the current point is counter-clockwise. If it is a clockwise or collinear turn, pop the last point from the stack. Repeat this check until a counter-clockwise turn is formed, then push the current point onto the stack.

## Complexity Analysis
- **Time Complexity**:
  - Finding the pivot: $O(N)$
  - Sorting the points: $O(N \\log N)$
  - Scanning phase: $O(N)$ (each point is pushed and popped at most once)
  - Total Time Complexity: $O(N \\log N)$
- **Space Complexity**: $O(N)$ to store the sorted points and the stack.