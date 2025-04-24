# 🧼 Bubble Sort Algorithm

This repository contains an implementation of the **Bubble Sort** algorithm, a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

## 📚 What is Bubble Sort?

Bubble Sort is a basic comparison-based sorting algorithm. It works by repeatedly swapping adjacent elements if they are in the wrong order. The largest values "bubble up" to the end of the list with each pass.

**Time Complexity:**
- Best Case: O(n)
- Average Case: O(n²)
- Worst Case: O(n²)

**Space Complexity:**
- O(1) – It’s an in-place sorting algorithm.

## 🧠 How It Works

1. Start at the beginning of the array.
2. Compare each pair of adjacent elements.
3. Swap them if they’re in the wrong order.
4. Repeat until no swaps are needed.

# ⚡ Quick Sort in Python

This repository contains a simple and clean implementation of the **Quick Sort** algorithm using Python.

Quick Sort is a **divide-and-conquer** sorting algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot.

---

## 📚 Algorithm Explanation

1. Select a pivot element.
2. Partition the array:
   - Move all elements less than or equal to the pivot to its left.
   - Move all elements greater than the pivot to its right.
3. Recursively apply the above steps to the sub-arrays.

**Time Complexity:**
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n²)

**Space Complexity:** O(log n) (for recursion stack)

# Selection Sort in Python 🧮

This is a simple Python script that demonstrates the **Selection Sort** algorithm. It takes user input to build a list of numbers and then sorts them in ascending order using Selection Sort.

## 📌 What is Selection Sort?

Selection Sort is a basic comparison-based sorting algorithm. It divides the input list into two parts: a sorted and an unsorted section. It repeatedly selects the smallest (or largest) element from the unsorted section and moves it to the end of the sorted section.

**Time Complexity:**
- Worst case: O(n²)
- Best case: O(n²)
- Space complexity: O(1)

## 🚀 How to Run

1. Clone this repository or download the `selection_sort.py` file.
2. Open your terminal or command prompt.
3. Run the script using Python:

```bash
python selection_sort.py

---

## 🖥️ Python Code

```python
def partition(array, lb, ub):
    pivot = array[lb]
    start = lb + 1
    end = ub

    while True:
        while start < end and array[start] <= pivot:
            start += 1

        while start <= end and array[end] > pivot:
            end -= 1

        if start < end:
            array[start], array[end] = array[end], array[start]
        else:
            break

    array[lb], array[end] = array[end], array[lb]
    return end

def quickSort(array, start, end):
    if start >= end:
        return
    
    k = partition(array, start, end)
    quickSort(array, start, k - 1)
    quickSort(array, k + 1, end)

# Input from user
n = int(input("How many elements: "))
data = [int(input(f"Enter your number {i+1} : ")) for i in range(n)]

print("Before sorting:", data)
quickSort(data, 0, len(data) - 1)
print("After sorting:", data)

## 🖥️ Example in Python

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        # Track if any swap happens
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(numbers))

