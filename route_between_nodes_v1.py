# JULY 17, 2019
# The following program is a solution to Cracking The Coding Interview: Question 4.1

# Route Between Two Nodes : Given a directed graph, design an algorithm to find out
# whether there is a route between two nodes.


# First we define an arbitrary graph using a python dictionary data structure.

graph = dict(A=['B', 'C'], B=['C', 'D'], C=['D'], D=['C'], E=['F'], F=['C'])

# this method will list the nodes in between the start node and the end node, provided a path exists between them.
def find_path(graph, start, end, path=[]):
    # append first node of interest to the list named 'path'.
    path = path+[start]
    # if the start node and end node of interest are equal.
    if start == end:
        return path
    # if the first node is not an element of the graph.
    if start not in graph:
        return None
    # if there is another node between the start point and end point, we append them to the graph list.
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return 'The path between ' + str(path[0]) + ' and ' + str(end) + ' is: ' + str(new_path)
            else:
                break
    return 'There is no path between ' + str(path[0]) + ' and ' + str(end)




if __name__ == "_main_":
    # enter start and in point within the find_path method
    print(find_path(graph, 'A', 'C'))