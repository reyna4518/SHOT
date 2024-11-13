def calculate_mean(bin_values):
    return sum(bin_values) / len(bin_values)

def equal_frequency_bins(data, num_bins):
    data_sorted = sorted(data)
    bin_size = len(data) // num_bins + 1
    return [data_sorted[i * bin_size: (i + 1) * bin_size] for i in range(num_bins)]

input_data = input("Enter a list of numbers separated by spaces: ")
data = list(map(int, input_data.split()))
num_bins = int(input("Enter the number of bins: "))

bins = equal_frequency_bins(data, num_bins)

print("Partition using equal frequency approach:")
for i, bin_values in enumerate(bins):
    print(f"Bin {i + 1}: {', '.join(map(str, bin_values))}")

bin_means = [calculate_mean(bin_values) for bin_values in bins]
smoothed_means = [mean for mean in bin_means for _ in range(len(bins[0]))]

print("\nSmoothing by bin means:")
for i, mean_value in enumerate(smoothed_means):
    print(f"Bin {i // len(bins[0]) + 1}: {mean_value}", end=", " if (i + 1) % len(bins[0]) != 0 else "\n")

print("\nSmoothing by bin boundaries:")
for i in range(num_bins):
    start_value, end_value = bins[i][0], bins[i][-1]
    print(f"Bin {i + 1}: {start_value}, {end_value}")
