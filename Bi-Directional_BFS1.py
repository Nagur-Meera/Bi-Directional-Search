from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    # Initialize frontiers
    front_start = {start: [start]}
    front_goal = {goal: [goal]}

    queue_start = deque([start])
    queue_goal = deque([goal])

    while queue_start and queue_goal:
        # Expand from start side
        current_start = queue_start.popleft()
        for neighbor, _ in graph[current_start]:
            if neighbor not in front_start:
                front_start[neighbor] = front_start[current_start] + [neighbor]
                queue_start.append(neighbor)
                if neighbor in front_goal:
                    return front_start[neighbor] + front_goal[neighbor][-2::-1]

        # Expand from goal side
        current_goal = queue_goal.popleft()
        for neighbor, _ in graph[current_goal]:
            if neighbor not in front_goal:
                front_goal[neighbor] = front_goal[current_goal] + [neighbor]
                queue_goal.append(neighbor)
                if neighbor in front_start:
                    return front_start[neighbor] + front_goal[neighbor][-2::-1]

    return None

Graph = {
    "A": [("F", 14), ("C", 9), ("B", 7)],
    "B": [("A", 7), ("C", 10), ("D", 15)],
    "C": [("A", 9), ("F", 2), ("B", 10), ("D", 11)],
    "D": [("B", 15), ("C", 11), ("E", 6)],
    "E": [("F", 9), ("D", 6)],
    "F": [("A", 14), ("C", 2), ("E", 9)]
}

bd_path = bidirectional_search(Graph, "A", "F")
print("Bi-directional Search Path:", bd_path)
