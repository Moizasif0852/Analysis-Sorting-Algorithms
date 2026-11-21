
import csv
import os
import matplotlib.pyplot as plt

results = {}

# Read benchmark results
with open("results/results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        case = row["Test Case"]
        algorithm = row["Algorithm"]
        time_taken = float(row["Average Time (Microseconds)"])

        if case not in results:
            results[case] = {}

        results[case][algorithm] = time_taken


# Create one graph for each test case
os.makedirs("results/graphs", exist_ok=True)

for case, algorithms in results.items():

    names = list(algorithms.keys())
    times = list(algorithms.values())

    plt.figure(figsize=(9, 5))

    plt.bar(names, times)

    plt.title(f"Sorting Algorithm Comparison - {case}")
    plt.xlabel("Sorting Algorithms")
    plt.ylabel("Average Time (Microseconds)")

    plt.xticks(rotation=15)
    plt.tight_layout()

    filename = case.lower().replace(" ", "_").replace("-", "")
    plt.savefig(f"results/graphs/{filename}.png", dpi=300)

    plt.close()

print("All 4 graphs generated successfully!")
print("Graphs saved in results/graphs/")
