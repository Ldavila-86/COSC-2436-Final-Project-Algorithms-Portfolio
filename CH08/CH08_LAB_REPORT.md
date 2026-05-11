### CH_08 Balanced Trees
- **Name:** Leiliany Davila
- **Date:** 04/02/2026
### Algorithm Analysis
#### AVL Trees
- **Balance Factor Range:** An AVL tree requires this value to stay within –1 and +1 for every node.
- **Why rebalance?** Rebalancing is necessary to prevent the tree from becoming unbalanced, which would increase its height and degrade performance. By rebalancing using rotations after insertions or deletions, an AVL tree ensures that operations remain efficient and the tree height stays logarithmic. This prevents the tree from becoming skewed and preserves fast search times.
- **Time Complexity (all operations):** O(log n)
#### Rotation Cases
| Case | Imbalance | Fix |
|------|-----------|-----|
| LL   |   Heavy left subtree of a heavy left child        | Right rotation on the root of subtree     |
| RR   | Heavy right subtree of a right child           |  Left rotation on the root of the subtree   |
| LR   |  Heavy right subtree of a left child         | Left rotation on left child, then right rotation on the root    |
| RL   | Heavy left subtree of a right child           |  right rotation on the right child, then a left rotation on the root   |
### Reflection Questions
1. Why is an unbalanced BST bad? - An unbalanced BST is bad because it leads to poor performance. In a balanced BST, the height of the tree is kept small, so operations such as searching, inserting, and deleting take O(log n) time. However, when a BST becomes unbalanced, its height can grow to O(n), causing these operations to degrade to linear time.
In the worst case, an unbalanced BST can resemble a linked list, where each node has only one child. This eliminates the efficiency benefit of using a tree structure and results in slower performance as the number of elements increases.
2. How do rotations maintain the BST property? - Tree rotations maintain the BST property because they preserve the in-order sequence of the nodes. During a rotation, only the parent-child relationships between a few nodes change, but the relative ordering of values remains the same.
3. What other self-balancing trees exist? - 
* AVL Trees – Maintain strict balance by ensuring the height difference between left and right subtrees is at most 1.
* Red-Black Trees – Use node coloring and rules to ensure the tree remains roughly balanced with guaranteed O(log n) operations.
* B-Trees – Balanced multi-way trees commonly used in databases and file systems.
Splay Trees – Automatically move recently accessed nodes closer to the root to improve access time over repeated operations.
