### Lab Report — Dijkstra's Shortest Path

**Student Information**
- **Name:** Leiliany Davila
- **Date:** 04/12/2026

### Algorithm Analysis: Dijkstra's Algorithm

#### Questions:
1. **What type of graph does this program build?**
   - Undirected, weighted graph.

2. **Why must all edge weights be non-negative for Dijkstra's to work?**
   - Dijkstra's algorithm assumes that once a node is visited, the shortest path to it is finalized. Negative weights can invalidate this assumption, leading to incorrect results.

#### Time Complexity:
- **With simple array scan for min-node:** O(V^2), where V is the number of vertices.
- **With a min-heap/priority queue:** O((V + E) log V), where E is the number of edges.

#### Core Data Structures:
| Structure      | Variable Name | What It Stores                                 |
|----------------|---------------|-------------------------------------------------|
| Adjacency dict | graph         | Connections and weights between nodes          |
| Cost table     | costs         | Current best-known costs to each node from start|
| Parent table   | parents       | Previous node on the shortest path to each node |
| Visited list   | processed     | Nodes whose shortest path has been finalized    |

#### Algorithm Trace:
Given nodes A, B, C, D and edges A-B(1), A-C(4), B-C(2), B-D(6), C-D(3), trace Dijkstra's from A to D.

| Iteration | Current Node | costs[A] | costs[B] | costs[C] | costs[D] | processed |
|-----------|--------------|----------|----------|----------|----------|-----------|
| Init      | —            | 0        | ∞        | ∞        | ∞        | —         |
| 1         | A            | 0        | 1        | 4        | ∞        | A         |
| 2         | B            | 0        | 1        | 3        | 7        | A, B      |
| 3         | C            | 0        | 1        | 3        | 6        | A, B, C   |
| 4         | D            | 0        | 1        | 3        | 6        | A, B, C, D|

**Shortest path A to D:** A -> B -> C -> D **Total cost:** 6

### Reflection Questions:

1. **Why does the algorithm initialize all node costs to infinity except the start node?**
   - To ensure any valid path is shorter than the initial presumed "infinite" path.

2. **Why do we store edges in both directions?**
   - To ensure easy traversal in an undirected graph.

3. **How would using a priority queue improve performance?**
   - Priority queues efficiently find the lowest cost node, reducing time complexity, especially beneficial for large graphs.

4. **What if a negative edge weight was introduced?**
   - Dijkstra's algorithm could produce incorrect results; Bellman-Ford algorithm handles negative weights.

5. **How does the parents dictionary allow path reconstruction?**
   - It stores the previous node, allowing backtracking to form the path.

6. **Why do we reverse the path at the end?**
   - It is constructed backwards, so reversing gives the correct order.

7. **What happens with disconnected components?**
   - If a destination's cost remains infinity, it is unreachable from the source, indicating disconnection.
