import csv
import math

def calDist(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def readFile(filePath):
    points = []
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            point = [int(row[0]), int(row[1])]
            points.append(point)
    return points

def writeFile(filePath, outputData):
    with open(filePath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(outputData)

points = readFile('input.csv')
n = len(points)

sumX = sum(points[i][0] for i in range(n))
sumY = sum(points[i][1] for i in range(n))
midPoint = [sumX / n, sumY / n]
print(f"Mid Point: {midPoint}")

outputData = [["", "p1", "p2", "p3", "p4", "C"]]
distanceList = []

for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(0)
        elif j < i:
            dist = calDist(points[i], points[j])
            row.append(dist)
            distanceList.append(dist)
        else:
            row.append("")
    outputData.append(["p" + str(i + 1)] + row)

midDistances = [calDist(midPoint, p) for p in points]
nearestPointIndex = min(range(n), key=lambda i: midDistances[i])
outputData.append(["C"] + midDistances + [0])

writeFile('output.csv', outputData)

print("\nDistance of each point from the center:")
for i, point in enumerate(points):
    print(f"Distance of p{i + 1} from centre: {midDistances[i]:.2f}")

print("\nNearest point from Centre is:", f"p{nearestPointIndex + 1}")

print("\nLower Triangular Distance Matrix:")
print("     ", end="")
for j in range(n):
    print(f"p{j + 1}  ", end="")
print()

for i in range(n):
    print(f"p{i + 1} ", end="")
    for j in range(n):
        if j < i:
            dist = calDist(points[i], points[j])
            print(f"{dist:.2f} ", end="")
        else:
            print("    ", end="")
    print()
print()
