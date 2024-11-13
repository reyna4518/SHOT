import csv

def correlation(x, y):
    if len(x) != len(y):
        raise ValueError("Lists x and y must have the same length")

    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum(i ** 2 for i in x)
    sum_y_sq = sum(i ** 2 for i in y)
    sum_xy = sum(x[i] * y[i] for i in range(n))

    numerator = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x_sq - sum_x ** 2) * (n * sum_y_sq - sum_y ** 2)) ** 0.5

    if denominator == 0:
        return 0

    return numerator / denominator

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            data.append([float(value) for value in row])
    return headers, data

def get_columns_to_correlate(headers):
    print("Available columns:")
    for i, header in enumerate(headers):
        print(f"{i}: {header}")
    
    while True:
        try:
            col1_index = int(input("Select the index of the first column to correlate: "))
            col2_index = int(input("Select the index of the second column to correlate: "))
            if col1_index < 0 or col2_index < 0 or col1_index >= len(headers) or col2_index >= len(headers):
                print("Invalid index. Please enter indices within the range.")
                continue
            break
        except ValueError:
            print("Please enter valid integer indices.")
    
    return col1_index, col2_index

file_path = input("Enter the path to the CSV file: ")
headers, data = read_csv(file_path)

col1_index, col2_index = get_columns_to_correlate(headers)

x = [row[col1_index] for row in data]
y = [row[col2_index] for row in data]

print("Correlation:", correlation(x, y))
