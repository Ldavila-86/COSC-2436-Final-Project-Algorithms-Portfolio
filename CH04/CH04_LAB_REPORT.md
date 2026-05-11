# Lab 04: Quicksort

## Student Information
- **Name:** Leiliany Davila
- **Date:** 2/19/2026

## Quicksort Concepts

### Divide and Conquer
Divide and conquer is a strategy where a problem is broken into smaller, easier parts. Each smaller part is solved on its own, and then the results are combined to solve the original problem. For example, in algorithms like quicksort, the list is divided around a pivot into items smaller than the pivot and items greater than the pivot, and each partition is sorted independently.

### The Three Steps
1. **Choose pivot:** Pick one value from the list. This value is called the pivot, and it’s what we use to compare the other items against.
2. **Partition:** Go through the list and split it into two groups: items smaller than the pivot and items greater than the pivot
3. **Recurse and combine:** Repeat the same steps on each smaller group until everything is broken down and sorted. Then put all the pieces back together:
sorted left side + pivot + sorted right side.

## Tracing Quicksort

### Trace: quicksort([3, 5, 2, 1, 4])
Initial Call
Array: [3, 5, 2, 1, 4]
Pivot: 3

Less → [2, 1]
Greater → [5, 4]


Sort Less [2, 1]
Pivot: 2

Less → [1]
Greater → []

Sorted → [1, 2]

Sort Greater [5, 4]
Pivot: 5

Less → [4]
Greater → []

Sorted → [4, 5]

final combination [1,2,3,4,5]

## Complexity Analysis

| Case | Time Complexity | Why? |
|------|----------------|------|
| Best | O(n log n) | The pivot splits the array evenly each time, so the work is balanced. |
| Average | O(n log n) | Most of the time the pivot makes the two sides “pretty even,” so recursion stays efficient. |
| Worst | O(n²) | Happens when the pivot is always the smallest or largest value, in other words a poor pivot. This poor pivot leads to one side being empty and the array barely shrinking. |

## Reflection Questions

- What happens if the array is already sorted and you always pick the first element as pivot?

You get the worst‑case because each pivot ends up at one end of the list.
The algorithm becomes slow and goes toward O(n²) behavior.

- How could you improve pivot selection to avoid worst-case performance?

Using a better pivot strategy such as: picking a random pivot or using the middle element.

- How does quicksort compare to other sorting algorithms you know (e.g., bubble sort, merge sort)?

*Quicksort is usually faster in practice because it works in place and has good average performance.*

*Merge sort is more stable and consistent (always O(n log n)) but uses extra memory. It is also the most similar to quicksort.*

*Bubble sort is much slower (O(n²)) and mainly used for teaching, not real‑world tasks.*

- Why do we use `array[1:]` instead of `array` when building the less and greater lists?

*Because array[0] is the pivot.
array[1:] skips the pivot so we don’t accidentally compare it with itself or duplicate it in the result.*
