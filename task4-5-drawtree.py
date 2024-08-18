from collections import deque
import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def heap_to_tree(heap, index=0):
    if index >= len(heap):
        return None

    node = Node(heap[index])

    left_index = 2 * index + 1
    right_index = 2 * index + 2

    node.left = heap_to_tree(heap, left_index)
    node.right = heap_to_tree(heap, right_index)

    return node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.clf()  # Очищення попереднього малюнка
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.pause(0.5)  # Оновлення в одному вікні

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def generate_colors(n):
    colormap = cm.get_cmap('Blues', n)  
    return [colormap(i) for i in np.linspace(0, 1, n)]

def reset_colors(node, default_color="skyblue"):
    # Рекурсивне скидання кольорів вузлів
    if node is not None:
        node.color = default_color
        reset_colors(node.left, default_color)
        reset_colors(node.right, default_color)

def dfs(tree_root):
    stack = [tree_root]
    visited = []
    total_nodes = count_nodes(tree_root)
    colors = generate_colors(total_nodes)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            node.color = colors[len(visited) - 1]
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            draw_tree(tree_root)

    plt.show()
    

def bfs(tree_root):
    queue = deque([tree_root])
    visited = []
    total_nodes = count_nodes(tree_root)
    colors = generate_colors(total_nodes)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            node.color = colors[len(visited) - 1]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            draw_tree(tree_root)

    plt.show()

# Приклад 
heap = [10, 5, 6, 2, 3, 7, 1]
root = heap_to_tree(heap)

print("DFS:")
plt.figure(figsize=(8, 5))  
dfs(root)  # Обхід у глибину

reset_colors(root)

print("BFS:")
plt.figure(figsize=(8, 5))
bfs(root)  # Обхід у ширину
