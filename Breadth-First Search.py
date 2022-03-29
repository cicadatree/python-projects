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

    #add your Firstnode to the the visited and queue lists
    visited.append(Firstnode)
    queue.append(Firstnode)

    while queue:
        m = queue.pop(0) #dequeue the next node in the queue list
        print (m, end = " ") # print the dequeued node in a single line

        
        for neighbour in graph[m]: # iterate over each neighbour of the dequed node
            if neighbour not in visited:  # if the neighbour hasn't yet been visited, append it to to the visited and queue lists
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '3') # call the function at a defined starting node