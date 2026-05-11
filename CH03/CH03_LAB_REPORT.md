# Lab 3: Recursion

## Student Information
- **Name:** Leiliany Davila
- **Date:** 2/15/2026

## Recursion Concepts

### Two Parts of Every Recursive Function
1. **Base Case:** 
    - The base case is a condition that stops the recursion. It's essential because it prevents infinite recursion and a possible stack overflow. For example, in the `countdown` function, the base case is when `i <= 0`.

2. **Recursive Case:** 
    - The recursive case is where the function calls itself with a smaller or simpler input. This step breaks the problem into smaller sub-problems. For example, in the `fact` function, the recursive case is `x * fact(x-1)`.

### The Call Stack
Explain how the call stack works with an example, such as `fact(3)`:

    ```plaintext
    fact(3)
      → 3 * fact(2)
          → 2 * fact(1)
              → returns 1
          → returns 2 * 1 = 2
      → returns 3 * 2 = 6

### **Reflection Questions**

 **1. What happens if you forget the base case?**
    - The function will continue calling itself forever, this means that a infinite recursion and a stack overflow error may occur.

 **2. Why is the naive Fibonacci implementation inefficient?**
    - Because it recalculates the same values many times. This leads to exponential time complexity O(2^n).
   
