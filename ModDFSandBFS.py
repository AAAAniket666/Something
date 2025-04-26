# Tree
# The tree structure is:
#         A
#       /    \
#      B       C
#    /  \     /  \
#   D    E   F    G
# / \   /   / \   /
# G  H A   I   J  L

 
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H','I'],  
    'E': ['A'],    # cycle: E -> A
    'F': ['J','K'],
    'G': ['L']
}


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


print("DFS Traversal:")
dfs(tree, 'A')  
print()  

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

print("BFS Traversal:")
bfs(tree, 'A')  
print()