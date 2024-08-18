import heapq
from collections import defaultdict

# Функція для реалізації алгоритму Дейкстри
def deikstra(graph, start):
    # Ініціалізація відстаней
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Створення графа
graph = defaultdict(dict)
graph['A']['B'] = 1
graph['A']['C'] = 4
graph['B']['C'] = 2
graph['B']['D'] = 5
graph['C']['D'] = 1
graph['D']['E'] = 3
graph['E'] = {}

start_vertex = 'A'
distances = deikstra(graph, start_vertex)

# Виведення результату
for vertex, distance in distances.items():
    print(f"Найкоротша відстань від {start_vertex} до {vertex} становить {distance}")
