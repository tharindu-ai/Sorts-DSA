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
