### Chapter 11: Knapsack Problem

**Student Information**

- Name: Leiliany Davila  
- Date: May 10, 2026  
- Course: COSC 2436

**Algorithm Summary**

- **How it works:**  
  The dynamic programming knapsack algorithm builds a grid that stores the best possible combination of items for every weight capacity from 0 up to the limit. At each step, it decides whether including the current item or excluding it gives a higher total value. The final solution is found at the bottom-right of the grid.

- **Time complexity:**  
  O(n × W), where n is the number of items and W is the capacity.

- **When to use it:**  
  This algorithm is best used when you need to maximize value under a weight constraint, such as budgeting, resource allocation, or packing problems where brute force would be too slow.

**Test Results**

- **Given Input:**  
  Capacity = 6  
  Items = guitar, stereo, laptop, iPhone, book, gold bar

- **Best Solution Found:**  
  Selected Items: Gold Bar, iPhone, Guitar, Laptop  
  Total Weight = 6  
  Total Value = $35,500

**Reflection Questions**

- **Why is dynamic programming more efficient than brute force for the knapsack problem?**  
  Dynamic programming avoids recomputing the same subproblems by storing intermediate results in a table. This significantly reduces the time complexity compared to brute force, which checks all possible combinations.

- **What is the main idea behind choosing between including or excluding an item?**  
  The algorithm compares the total value of two choices: including the item or excluding it. It always selects the option that provides the higher value while staying within the weight limit.

- **What would happen if the capacity increases significantly?**  
  If capacity increases, the grid size grows, which increases time and memory usage. However, the algorithm still remains efficient compared to brute force and can handle reasonable increases in capacity.

**Challenges Encountered**

One challenge was understanding how the 2D grid stores partial solutions and how each cell represents a decision point. Initially, it was confusing to track how previous results were reused to build new ones. This was resolved by carefully tracing small examples step by step and observing how including or excluding items affected the total value.
