--- README.md (原始)


+++ README.md (修改后)
# ✨ Sorting Algorithms Comparison

An interactive project built with **Streamlit** to compare and visualize the performance of various sorting algorithms.

## 📋 Features

- 🎯 Support for 6 sorting algorithms:
  - **Bubble Sort**
  - **Insertion Sort**
  - **Merge Sort**
  - **Selection Sort**
  - **Quick Sort**
  - **Heap Sort**

- 📊 Visual comparison of algorithm execution times
- ⏱ Execution time measurement for each algorithm
- 🎨 Beautiful and responsive user interface

## 🚀 Installation & Running

### Prerequisites

- Python 3.7+
- pip

### Install Dependencies

```bash
pip install streamlit matplotlib
```

### Run the Application

```bash
streamlit run app.py
```

## 📁 Project Structure

```
├── app.py              # Main Streamlit application
├── bubble_sort.py      # Bubble Sort implementation
├── insertion_sort.py   # Insertion Sort implementation
├── merge.py            # Merge Sort implementation
├── selection_sort.py   # Selection Sort implementation
└── README.md           # Project documentation
```

## 💡 How to Use

1. Run the application
2. Select an algorithm from the list
3. Enter your numbers (separated by spaces)
4. Click the "Sort" button
5. View the sorted result and execution time

### Performance Comparison

To compare the execution time of all algorithms:
1. Use the slider to select the number of random elements
2. Click the "Draw Comparison Chart" button
3. View the bar chart showing execution time for each algorithm

## 📊 Time Complexity of Algorithms

| Algorithm | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) |

## 🛠 Developer

This project was created for educational purposes to demonstrate the performance differences between sorting algorithms.

## 📄 License

This project is free to use for educational purposes without any restrictions.
