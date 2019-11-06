from aspect import weave
import sys


class Vertex(object):
    """ This class helps to create a Vertex for our graph """

    def __init__(self, key):
        self.key = key
        self.edges = {}

    def addNeighbour(self, neighbour, weight=0):
        self.edges[neighbour] = weight

    def __str__(self):
        return str(self.key) + 'connected to: ' + str([x.key for x in self.edges])

    def getEdges(self):
        return self.edges.keys()

    def getKey(self):
        return self.key

    def getWeight(self, neighbour):
        try:
            return self.edges[neighbour]
        except:
            return None


class Graph(object):
    """ This class helps to create Graph with the help of created vertexes """

    def __init__(self):
        self.vertexList = {}
        self.count = 0

    def addVertex(self, key):
        self.count += 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def getVertex(self, vertex):
        if vertex in self.vertexList:
            return self.vertexList[vertex]
        else:
            return None

    def addEdge(self, fromEdge, toEdge, cost=0):
        if fromEdge not in self.vertexList:
            newVertex = self.addVertex(fromEdge)
        if toEdge not in self.vertexList:
            newVertex = self.addVertex(toEdge)
        self.vertexList[fromEdge].addNeighbour(self.vertexList[toEdge], cost)

    def getVertices(self):
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())


def getDict(file):
    words = set()
    with open(file) as d:
        for w in d.read().split("\n"):
            words.add(w.lower())
    return words


def isEng(word):
    englishWords = getDict("dictionary.txt")
    if word in englishWords:
        return True
    return False


def permutations(xl, length=-1, res=[], output=[]):
    if xl == [] or len(res) == length:
        output.append(res)
        return
    for i in range(len(xl)):
        permutations(xl[:i] + xl[i + 1:], length, res + [xl[i]], output)
    return output


if __name__ == '__main__':
    # Weave
    weave(sys.modules[__name__])

    # Test Graph
    graph = Graph()
    graph.addVertex('A')
    graph.addVertex('B')
    graph.addVertex('C')
    graph.addVertex('D')

    graph.addEdge('A', 'B', 5)
    graph.addEdge('A', 'C', 6)
    graph.addEdge('A', 'D', 2)
    graph.addEdge('C', 'D', 3)

    for vertex in graph:
        for vertexes in vertex.getEdges():
            print('({}, {}) => {}'.format(vertex.getKey(), vertexes.getKey(), vertex.getWeight(vertexes)))

    # OUTPUT:
    # (C, D) => 3
    # (A, C) => 6
    # (A, D) => 2
    # (A, B) => 5

    # Test Generator

    found = set()
    letters = "abc"
    for sz in range(2, len(letters) + 1):
        print("\nSize:", sz, "letters")
        for comb in permutations(letters, sz, [], []):
            if isEng("".join(comb)) and not "".join(comb) in found:
                print("Found word:", "".join(comb))
                found.add("".join(comb))
    print()


