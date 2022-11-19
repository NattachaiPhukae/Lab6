GraphList = {}
GraphMatrix = []
GraphEdge = []
GraphNumber = []


def create_node(listOfNodes: list):
    # add list of nodes to GraphNumber
    GraphNumber.extend(listOfNodes)

    # create nodes in adjacency matrix
    nowSize = len(GraphMatrix)
    addSize = len(listOfNodes)
    for node in listOfNodes:
        GraphMatrix.append([0 for i in range(nowSize)])
    for list_ in GraphMatrix:
        list_ += [0 for _ in range(addSize)]

    # create nodes in adjacency list
    for node in listOfNodes:
        GraphList[node] = list()

    # create nodes in edge list (no need)


def connect(start: str, end: str):
    # add edge to adjacency matrix
    start_index = GraphNumber.index(start)
    end_index = GraphNumber.index(end)
    GraphMatrix[start_index][end_index] = 1
    GraphMatrix[end_index][start_index] = 1

    # add edge to adjacency list
    GraphList[start].append(end)
    GraphList[end].append(start)

    # add edge to edge list
    GraphEdge.append([start, end])


def disconnect(start: str, end: str):
    # remove edge from adjacency matrix
    start_index = GraphNumber.index(start)
    end_index = GraphNumber.index(end)
    GraphMatrix[start_index][end_index] = 0
    GraphMatrix[end_index][start_index] = 0

    # remove edge from adjacency list
    GraphList[start].remove(end)
    GraphList[end].remove(start)

    # remove edge from edge list
    GraphEdge.remove([start, end])


def display():
    print("Adjacency Matrix")
    print("  ", end="")
    print(*GraphNumber)
    index = 0
    for i in GraphMatrix:
        print(GraphNumber[index], end=" ")
        print(*i)
        index += 1
    print("Adjacency List")
    for key, value in GraphList.items():
        print(key, "->", value)
    print("Edge List")
    index = 0
    for i in GraphEdge:
        print(index, "->", *i)
        index += 1


def reset():
    global GraphList, GraphMatrix, GraphEdge, GraphNumber
    GraphList = {}
    GraphMatrix = []
    GraphEdge = []
    GraphNumber = []


def Example1():
    reset()
    create_node(["A", "B", "C", "D"])
    connect("A", "B")
    connect("A", "C")
    connect("B", "C")
    connect("C", "D")
    display()


def Example2():
    reset()
    create_node(["A", "B", "C", "D", "E", "F"])
    connect("A", "B")
    connect("A", "C")
    connect("A", "F")
    connect("C", "D")
    connect("D", "E")
    connect("E", "F")
    display()


def Example3():
    reset()
    create_node(["A", "B", "C", "D", "E", "F"])
    connect("A", "B")
    connect("A", "C")
    connect("C", "D")
    connect("C", "F")
    connect("E", "F")
    print("-----Part 1-----")
    display()
    disconnect("C", "F")
    disconnect("A", "B")
    disconnect("C", "D")
    print("-----Part 2-----")
    display()
    connect("A", "E")
    connect("B", "C")
    connect("D", "F")
    print("-----Part 3-----")
    display()


def main():
    print("Welcome to Graphs\nWhat do you want to see? (1, 2 or 3)")
    inp = input(": ")
    if inp == "1":
        Example1()
    elif inp == "2":
        Example2()
    elif inp == "3":
        Example3()


main()