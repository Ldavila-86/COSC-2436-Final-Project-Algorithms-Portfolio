# Lab 06: BFS

## Student Information
- **Name:** Leiliany Davila
- **Date:** 3/3/2026

## Key Concepts
1. **Graphs:** A structure made up of nodes and edges. They can be either directed or undirected.
2. **Direct graph:** A directed graph will have edges that will go in ne direction only, like a one-way street.
3. **Undirected graph:** An undireted graph will have nodes going in both directions, like a two-way street
4. **BFS(Breadth‑First Search):** This search focuses on the FIFO (First in, First out) method. Meaning that it  visits the closest nodes first and works level by level, making it useful for finding the shortest path in an unweighted graph.
5. **DFS (Depth‑First Search):** This search goes as far as possible in one direction before backtracking, like going down a road until one hits a dead end.
6. **Adjacency list:** Stores each node and a list of its neighbors, keeping data organized and efficient.

## What I Learned
One of the things I learned feom this lab is how to implement the BFS algorithm to explore nodes level by level and find the shortest path in unweighted graphs.

## Challenges
I followed the instructions, so the code part was not hard. But I am still having problems with formating. Good thing that the AI can fix my formating mistakes.

## Reflection Questions
1. **Why does BFS use a queue instead of a stack?**
-BFS processes nodes level by level, exploring neighbors first, with what we call a FIFO (First In, First Out) queue. Stacks, on the other hand uses LIFO (Last In, First Out). The approach of stacks would actually dive deeper than the queue in BFS, meaning it may explore unnecessary pathways to the shortest path.
2. **What is the difference between BFS shortest path and actual shortest distance?**
-For BFS to say that they have found the shortest path, it means that they have visited the least ammount of nodes possible. Each edge in the case of an unweighted graph "costs" the same so, from node to node the edges are worth a weight of 1.
In the case of the actual shortest distance, the edges will have different weights or costs. Meaning that the distance will have an actual value, unlike the unweighted graphs. For example: A -(100)- B -(20)- C = 120.  The path from A to C has a distance of 120, while from B to C it is 20.


3. **When would you use BFS vs DFS?**
-BFS would be best used for finding shortest paths in unweighted graphs, checking if a graph is connected, and exploring layer-by-layer in things like social networks. 
And, DFS when you need to explore as far as possible, meaning it would be useful for topological sorts, detecting cycles, and  connectivity checks.
