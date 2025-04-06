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
    "A": [("B", 4), ("C", 5)],
    "B": [("A", 4), ("C", 11), ("D", 9), ("E", 7)],
    "C": [("A", 5), ("B", 11), ("E", 3)],
    "D": [("B", 9), ("E", 13), ("F", 2)],
    "E": [("B", 7), ("C", 3), ("D", 13), ("F", 6)],
    "F": [("D", 2), ("E", 6)]
}

bd_path = bidirectional_search(Graph, "A", "F")
print("Bi-directional Search Path:", bd_path)
