import csv
import heapq
from collections import defaultdict

# Load graph from CSV
def load_graph(filename):
    graph = defaultdict(list)
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            src = row['source']
            dest = row['destination']
            dist = int(row['distance'])
            
            graph[src].append((dest, dist))
            graph[dest].append((src, dist))  # Undirected graph
    
    return graph


# Dijkstra's Algorithm
def dijkstra(graph, start):
    priority_queue = [(0, start)]  # (cost, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        
        if current_cost > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_cost + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


# Run program
if __name__ == "__main__":
    graph = load_graph("india_cities_distances.csv")
    
    start_city = input("Enter starting city: ")
    shortest_paths = dijkstra(graph, start_city)
    
    print("\nShortest distances from", start_city)
    for city, distance in shortest_paths.items():
        print(f"{city}: {distance} km")
