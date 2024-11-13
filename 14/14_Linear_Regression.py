import csv

def linearRegression(x, y):
    n = len(x)
    sumX = sum(x)
    sumY = sum(y)
    sumXY = 0
    sumXX = 0

    for i in range(n):
        sumXY += x[i] * y[i]
        sumXX += x[i] ** 2

    a = (sumY * sumXX - sumX * sumXY) / (n * sumXX - sumX ** 2)
    b = (n * sumXY - sumX * sumY) / (n * sumXX - sumX ** 2)

    return a, b

def readFile(filePath):
    with open(filePath, mode='r') as file:
        robj = csv.reader(file)
        headers = next(robj)
        data = list(robj)
    
    return headers, data

def extractColumn(data, index):
    return [float(row[index]) for row in data]

def main():
    filePath = "Folds5x2_pp.csv"
    headers, data = readFile(filePath)
    
    print("Available columns:")
    for i, header in enumerate(headers):
        print(f"{i}: {header}")
    
    x_index = int(input("Enter the index number for the x column: ").strip())
    y_index = int(input("Enter the index number for the y column: ").strip())

    x = extractColumn(data, x_index)
    y = extractColumn(data, y_index)

    slope, intercept = linearRegression(x, y)
    print(f"Slope (m): {slope:.2f}")
    print(f"Intercept (c): {intercept:.2f}")

if __name__ == "__main__":
    main()
