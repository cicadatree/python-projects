# Graph Visualized:
#        5
#       / \
#      3   7
#     / \   \
#    2   4---8

graph = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
} # represents the children of each node

visited = [] # initaite list for visited nodes
queue = [] # initialize list for the queue

def bfs(visited, graph, Firstnode): # breadth-first search function;
    visited.append(Firstnode)
    queue.append(Firstnode)

    while queue:
        m = queue.pop(0)
        print (m, end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
print("Following is the Breadth-Frist Search")
bfs(visited, graph, '3') # call the function