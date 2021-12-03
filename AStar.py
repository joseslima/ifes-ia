class AStar:
    def __init__(self, map):
        self.map = map
        
    def initialize(self, startNode, goal):
        self.path = { startNode: None}
        self.costMap = { startNode: self.estimateDistance(startNode, goal) }
        self.openList = [startNode]
        self.closedList = []
        self.distance = 0

    def nextNodes(self, currentNode):
        i = currentNode[0]
        j = currentNode[1]

        nextNodes = []
        if i > 0 and self.map[i - 1][j] != '1':
            nextNodes.append((i - 1, j))

        if (i + 1) < len(self.map) and self.map[i + 1][j] != '1':
            nextNodes.append((i + 1, j))

        if j > 0 and self.map[i][j - 1] != '1':
            nextNodes.append((i, j - 1))

        if (j + 1) < len(self.map[0]) and self.map[i][j + 1] != '1':
            nextNodes.append((i, j + 1))

        return nextNodes

    def getBest(self):
        currentIndex = 0
        bestHeuristic = self.costMap[self.openList[currentIndex]]

        for index, node in enumerate(self.openList):
            if (self.costMap[node] < bestHeuristic):
                bestHeuristic = self.costMap[node]
                currentIndex = index

        bestNode = self.openList[currentIndex]

        self.openList.remove(bestNode)
        self.closedList.append(bestNode)

        return bestNode
    
    def estimateDistance(self, currentNode, goal):
        return abs(currentNode[0] - goal[0]) + abs(currentNode[1] - goal[1])

    def generatePath(self, node):
        path = [node]
        while self.path[node] != None:
            path.append(self.path[node])
            node = self.path[node]
        return path[::-1]


    def getPath(self, startNode, goal):
        self.initialize(startNode, goal)

        while self.openList:
            currentNode = self.getBest()

            if (currentNode == goal):
                return self.generatePath(currentNode)

            for nextNode in self.nextNodes(currentNode):
                if nextNode not in self.closedList and nextNode not in self.openList:
                    self.openList.append(nextNode)
                    if nextNode not in self.costMap.keys():
                        self.distance += 1
                        self.costMap[nextNode] = self.estimateDistance(nextNode, goal) + self.distance
                        self.path[nextNode] = currentNode

        return self.generatePath(currentNode)

