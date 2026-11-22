from typing import List, Tuple


def radial_search(points: List[Tuple[float, float]], center: Tuple[float, float], radius: float) -> List[Tuple[float, float]]:
    result = []
    center_x, center_y = center
    radius_squared = radius ** 2
    for point in points:
        point_x, point_y = point
        distance_squared = (point_x - center_x) ** 2 + (point_y - center_y) ** 2
        if distance_squared <= radius_squared:
            result.append(point)
    return result