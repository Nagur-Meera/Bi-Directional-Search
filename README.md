# 🔄 Bi-Directional Search - Pathfinding Algorithm

## 📌 Problem Statement

Given an undirected graph represented as an **adjacency list**, the task is to find a **valid path** between a **source node `s`** and a **target node `t`** using **Bi-Directional Search**.

> 📍 In this problem:  
> - Start Node (`s`) = A  
> - Goal Node (`t`) = F  

---

## 🧠 Algorithm: Bi-Directional Search

### ✅ Description:

Bi-Directional Search is a search strategy that simultaneously performs **Breadth-First Search (BFS)** from the **start node** and the **goal node**. The search stops when the two searches **meet in the middle**.

It is more efficient than standard BFS for large graphs, especially when the solution is expected to lie midway between `start` and `goal`.

⚠️ Note: Bi-Directional Search does **not guarantee the optimal path** in weighted graphs. It is mainly suited for **unweighted graphs** or cases where **any path is acceptable**.

---

## 🔽 Step-by-Step Procedure:

1. **Initialize two queues:**
   - `queue_start` for the forward search (from start)
   - `queue_goal` for the backward search (from goal)

2. **Track paths** for each node visited from both directions:
   - `front_start[node] = path from start to node`
   - `front_goal[node] = path from goal to node`

3. Loop until both queues are non-empty:
   - Expand one level from the **start side**:
     - For each neighbor, if not already visited:
       - Record path
       - If it exists in `front_goal`, merge and return full path.
   - Expand one level from the **goal side** similarly.

4. If queues are exhausted and no intersection is found, return `None`.

---


## 🗺 Sample Graph (Adjacency List):

```python
Graph = {
    "A": [("F", 14), ("C", 9), ("B", 7)],
    "B": [("A", 7), ("C", 10), ("D", 15)],
    "C": [("A", 9), ("F", 2), ("B", 10), ("D", 11)],
    "D": [("B", 15), ("C", 11), ("E", 6)],
    "E": [("F", 9), ("D", 6)],
    "F": [("A", 14), ("C", 2), ("E", 9)]
}
