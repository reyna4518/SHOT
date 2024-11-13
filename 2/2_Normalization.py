import csv

def readFile(filePath):
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        columns = {header: [] for header in headers}
        for row in reader:
            for i, value in enumerate(row):
                columns[headers[i]].append(float(value))
    return headers, columns

def writeFile(filePath, headers, originalData, minMaxData, zScoreData, columnToNormalize=None):
    with open(filePath, 'w', newline='') as file:
        writer = csv.writer(file)
        if columnToNormalize:
            newHeaders = [f"{columnToNormalize} (Original)", f"{columnToNormalize} (Min-Max)", f"{columnToNormalize} (Z-Score)"]
            writer.writerow(newHeaders)
            for i in range(len(originalData)):
                row = [f"{originalData[i]:.2f}", f"{minMaxData[i]:.2f}", f"{zScoreData[i]:.2f}"]
                writer.writerow(row)
        else:
            newHeaders = []
            for header in headers:
                newHeaders.extend([f"{header} (Original)", f"{header} (Min-Max)", f"{header} (Z-Score)"])
            writer.writerow(newHeaders)
            num_rows = len(originalData[headers[0]])
            for i in range(num_rows):
                row = []
                for header in headers:
                    row.extend([f"{originalData[header][i]:.2f}", f"{minMaxData[header][i]:.2f}", f"{zScoreData[header][i]:.2f}"])
                writer.writerow(row)

def minMax(data, minValue=0, maxValue=1):
    minOriginal = min(data)
    maxOriginal = max(data)
    return [(x - minOriginal) * (maxValue - minValue) / (maxOriginal - minOriginal) + minValue for x in data]

def zScore(data):
    mean = sum(data) / len(data)
    stdDev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [(x - mean) / stdDev for x in data]

def normalize(ipfilePath, opFilePath):
    headers, columns = readFile(ipfilePath)
    print("Available columns for normalization:")
    for i, header in enumerate(headers):
        print(f"{i + 1}. {header}")
    print(f"{len(headers) + 1}. Normalize all columns")

    selectedColumnIndex = int(input("Enter the column number to normalize (or select option to normalize all): ")) - 1

    if selectedColumnIndex == len(headers):
        minMaxResults = {}
        zScoreResults = {}
        for header in headers:
            minValue = float(input(f"Enter new minimum value for {header}: "))
            maxValue = float(input(f"Enter new maximum value for {header}: "))
            colData = columns[header]
            minMaxResults[header] = minMax(colData, minValue, maxValue)
            zScoreResults[header] = zScore(colData)
        writeFile(opFilePath, headers, columns, minMaxResults, zScoreResults)
        print(f"Original, Min-Max, and Z-Score normalized values saved to {opFilePath}")
    else:
        columnToNormalize = headers[selectedColumnIndex]
        minValue = float(input("Enter the new minimum value for Min-Max scaling: "))
        maxValue = float(input("Enter the new maximum value for Min-Max scaling: "))
        colData = columns[columnToNormalize]
        minMaxResult = minMax(colData, minValue, maxValue)
        zScoreResult = zScore(colData)
        writeFile(opFilePath, headers, colData, minMaxResult, zScoreResult, columnToNormalize)
        print(f"Original, Min-Max, and Z-Score normalized values saved to {opFilePath}")

inputFilePath = 'Folds5x2_pp.csv'
outputFilePath = 'output.csv'
normalize(inputFilePath, outputFilePath)