# Lab 2: Selection Sort

## Student Information
- **Name:** Leiliany Davila
- **Date:** 2/8/26

## Algorithm Summary

### Selection Sort
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **How it works:** 
  - Repeatedly find the smallest element from the unsorted part of the list and move it to the beginning.
  
### Python's Built-in Sort (Timsort)
- **Time Complexity:** O(n log n)

## Array vs Linked List Analysis

| Operation | Array | Linked List | Explanation |
|-----------|-------|-------------|-------------|
| Read      | O(1)  | O(n)        | Arrays provide direct access |
| Insert    | O(n)  | O(1)        | Linked lists are faster at inserting at head |
| Delete    | O(n)  | O(1)*       | Fast deletes at head in linked lists |

* O(1) only at head; O(n) to find other positions.

## Test Results
- **Top 5 Smallest Cities by Population:**
  1. McAllen: 142,210
  2. Pasadena: 151,950
  3. Killeen: 153,095
  4. Brownsville: 183,392
  5. McKinney: 195,308

- **Top 5 Largest Cities by Population:**
  1. Houston: 2,304,580
  2. San Antonio: 1,547,253
  3. Dallas: 1,304,379
  4. Austin: 978,908
  5. Fort Worth: 918,915

## Reflection Questions

1. **Why is selection sort O(n²)?**
   - It performs nested iterations over the list, resulting in n * (n - 1) comparisons in the worst case.

2. **When would you choose a linked list over an array?**
   - When frequent insertion and deletion at the head are required without shifting elements.

3. **Why does Python use arrays (lists) as the default sequence type?**
   - Arrays provide efficient random access and are generally more efficient space-wise compared to linked lists.

---
