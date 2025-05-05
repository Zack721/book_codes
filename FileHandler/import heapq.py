import heapq

def dijkstra(graph, start):
    # Distance from start to node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Priority queue to hold nodes to explore
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if we found a better path already
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph: adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(f"Shortest distances from node {start_node}:")
for node, distance in shortest_paths.items():
    print(f"  {node}: {distance}")
