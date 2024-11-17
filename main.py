import random
points = [(random.uniform(0, 20), random.uniform(0, 20)) for _ in range(5)]
distances = []

def euclideanDistance(points):
    for x1, y1 in points:
        for x2, y2 in points:
            if (x1, y1) == (x2, y2):
                continue
            distances.append(((x1 - x2)**2 + (y1 - y2)**2)**0.5)

euclideanDistance(points)
print("Points:")
print("\n".join(map(str, points)))
print("Minimum distance between points: ", min(distances))
