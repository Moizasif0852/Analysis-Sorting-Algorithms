# Empirical Analysis of Sorting Algorithms

## Overview

This project implements and compares four sorting algorithms using Python. The objective is to analyse their execution time, number of comparisons, swaps, and auxiliary space requirements under different input conditions.

## Algorithms Implemented

1. Selection Sort
2. Bubble Sort
3. Quick Sort
4. Merge Sort

## Experimental Setup

The algorithms were tested using four input cases:

- 5 elements (Sorted)
- 5 elements (Reverse Sorted)
- 100 elements (Sorted)
- 100 elements (Reverse Sorted)

Each experiment was performed three times, and the average execution time was calculated.

## Technologies Used

- Python
- Matplotlib
- CSV
- VS Code

## Project Structure

```text
Assignment_3/
│
├── algorithms/
│   ├── selection_sort.py
│   ├── bubble_sort.py
│   ├── quick_sort.py
│   └── merge_sort.py
│
├── results/
│   ├── results.csv
│   └── graphs/
│
├── main.py
├── benchmark.py
├── generate_graphs.py
├── README.md
└── .gitignore
```

## Installation and Execution

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Assignment_3
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install matplotlib
```

### 5. Run the algorithms

```bash
python main.py
```

### 6. Run the benchmark

```bash
python benchmark.py
```

### 7. Generate graphs

```bash
python generate_graphs.py
```

## Results

Benchmark results are saved in `results/results.csv`.

The generated graphs are saved in `results/graphs/`.

## Conclusion

The experiment demonstrates that algorithm performance depends on input size and input arrangement. Merge Sort performed best on the tested 100-element datasets, while simpler algorithms were competitive for the small datasets.
