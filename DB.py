# DFS and BFS traversal with user input
def get_graph_from_user():
    print("Enter the number of nodes:")
    n = int(input())
    print("Enter the node names (space separated):")
    nodes = input().split()
    tree = {node: [] for node in nodes}
    print("Enter the number of edges:")
    e = int(input())
    print("Enter each edge as: parent child (space separated)")
    for _ in range(e):
        u, v = input().split()
        if u in tree:
            tree[u].append(v)
        else:
            tree[u] = [v]
    print("Enter the starting node:")
    start_node = input().strip()
    return tree, start_node


def dfs(tree, node, visited=None):
    
    if visited is None:
        visited = set()
    
    # If the node is already visited, return immediately to avoid a cycle.
    if node in visited:
        return

    # Mark the current node as visited and process it.
    visited.add(node)
    print(node, end=' ')

    # Recurse for each child.
    for child in tree.get(node, []):
        dfs(tree, child, visited)


def bfs(tree, start):
   
    visited = {start}  # Initialize visited set with the start node.
    queue = [start]    # Initialize the queue with the start node.
    
    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        
        # Process each child of the current node.
        for child in tree.get(node, []):
            # Only enqueue children that haven't been visited.
            if child not in visited:
                visited.add(child)
                queue.append(child)


tree, start_node = get_graph_from_user()

print("DFS Traversal:")
dfs(tree, start_node)
print()

print("BFS Traversal:")
bfs(tree, start_node)
print()