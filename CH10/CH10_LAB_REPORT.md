## Student Information
**Name:** Leiliany Davila  
**Date:** 04/19/26 

**Algorithm Analysis:** Greedy Truck Packing Algorithm  

---

# Algorithm Understanding

**What type of problem is this algorithm solving?**  
This algorithm addresses a packing problem, specifically an approximation problem using a greedy strategy.

**Is this greedy algorithm guaranteed to produce the optimal solution? Why or why not?**  
No, greedy algorithms do not guarantee optimal solutions because they make local optimal choices at each step without considering the entire problem space.

**What is the greedy choice made in this algorithm?**  
The algorithm chooses to pack the largest available box (by volume) that fits, maximizing immediate space usage.

---

# Implementation Questions

**Why do we sort the boxes in descending order of volume before packing?**  
Sorting in descending order allows the algorithm to prioritize larger boxes, filling space more quickly and efficiently.

**What would happen if we sorted the boxes in ascending order instead?**  
Sorting in ascending order would likely lead to inefficient space usage, as smaller boxes would be packed first, leaving less room for larger boxes.

**Why do we keep track of `used_volume`?**  
Tracking `used_volume` helps ensure that we do not exceed the truck's capacity, maintaining the constraint of the available volume.

---

# Extension: Dimension Constraints

**Why is checking only volume not sufficient for real-world packing?**  
In real-world scenarios, a box might fit by volume but not by shape or orientation constraints.

**Give an example where a box fits by volume but not by dimensions.**  
A long, narrow box may have the same volume as a shorter, wider box but may not fit within the truck's specific dimensions.

**How would you modify the algorithm to check dimension constraints before packing a box?**  
You can add a condition to evaluate whether each box fits within the truck's dimensions before adding it to the list of packed boxes.

---

# Reflection Questions

**What is a limitation of this greedy approach? Provide a scenario where it fails to find the optimal solution.**  
The greedy algorithm may leave small gaps that could have been filled with precise combinations of smaller boxes.

**How is this problem related to the Knapsack Problem?**  
Both involve selecting items to maximize usage within constraints like space or weight.

**What type of algorithm would guarantee an optimal solution for this problem? What is the tradeoff?**  
A dynamic programming algorithm could guarantee an optimal solution but would have higher computational requirements.

**If the truck had weight limits in addition to volume, how would the algorithm need to change?**  
The algorithm would need to track both volume and weight, only adding boxes that meet both constraints.

**Why are greedy algorithms often preferred despite not always being optimal?**  
They are computationally efficient and simpler to implement, making them suitable for approximations in complex problems.
