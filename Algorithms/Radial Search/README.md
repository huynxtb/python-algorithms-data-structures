# Radial Search

## Introduction
Radial Search is an algorithm designed to efficiently find all points within a specified radius from a given center point in a two-dimensional space. This algorithm is particularly useful in applications such as geographical data analysis, clustering, and spatial queries where proximity is a key factor.

## Usage
Here is a simple example of how to use the `radial_search` function:


points = [(1, 2), (2, 3), (3, 4), (5, 5)]
center = (2, 2)
radius = 2.0
result = radial_search(points, center, radius)
print(result)  # Output: [(1, 2), (2, 3)]


## Detailed Explanation
The `radial_search` function takes three parameters: a list of points, a center point, and a radius. It calculates the squared distance from each point to the center point to avoid computing the square root, which is computationally expensive. If the squared distance is less than or equal to the squared radius, the point is considered to be within the specified radius and is added to the result list. Finally, the function returns the list of points that are within the radius.

## Complexity Analysis
- **Time Complexity:** O(n), where n is the number of points. The algorithm iterates through each point once to check its distance from the center.
- **Space Complexity:** O(k), where k is the number of points within the radius. The space used is proportional to the number of points that meet the criteria.