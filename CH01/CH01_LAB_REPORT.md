# Chapter 1 Lab Report: Binary Search

## Student Information

**Name:** Leiliany Davila

**Date:** 5/9/26

**Course:** COSC 2436



## Algorithm Summary

### Linear Search
Linear search works by going through a list one element at a time until it finds the value you’re looking for or reaches the end. It basically checks every item in order from start to finish.
The time complexity is O(n), which means the bigger the list gets, the longer it takes, since it might have to check every single element.
Linear search is best to use when the dataset is small or when the list is not sorted, because it doesn’t depend on any specific order.

### Binary Search
Binary search works by repeatedly dividing a sorted list in half. It starts by checking the middle value. If the target is smaller, it looks at the left half; if it’s bigger, it looks at the right half. It keeps doing this until it finds the value or runs out of elements.
The time complexity is O(log n), which is much faster than linear search for large datasets because it reduces the search space by half each time.
Binary search should only be used on sorted data, because it relies on the list being in order to know which half to eliminate.

## Test Results
* **List size:** 100
- Linear Search Time: 0.00012 seconds
- Binary Search Time: 0.00001 seconds

* **List size:** 1,000
- Linear Search Time: 0.00135 seconds
- Binary Search Time: 0.00002 seconds

* **List size:** 10,000
- Linear Search Time: 0.01350 seconds
- Binary Search Time: 0.00003 seconds

* **List size:** 100,000
- Linear Search Time: 0.14020 seconds
- Binary Search Time: 0.00004 seconds

From these results, I can see that linear search takes longer as the list gets bigger, while binary search stays very fast even with large lists. This shows that binary search is way more efficient, as long as the data is sorted.
