import math


class Node:
    id = None  # Unique value for each node.
    up = None  # Represents value of neighbors (up, down, left, right).
    down = None
    left = None
    right = None
    previousNode = None  # Represents value of neighbors.
    edgeCost = None  # Represents the cost on the edge from any parent to this node.
    gOfN = None  # Represents the total edge cost
    hOfN = None  # Represents the heuristic value
    heuristicFn = None  # Represents the value of heuristic function

    def __init__(self, value):
        self.value = value


maze_list = []
maze_nodes = [Node(0)]
maze_nodes.clear()
maze_nodes_2d = []
maze_nodes_2d.clear()
dfs_visited = [Node(0)]
dfs_visited.clear()
dfs_not_visited = [Node(0)]
dfs_not_visited.clear()
bfs_visited = [Node(0)]
bfs_visited.clear()
bfs_not_visited = [Node(0)]
bfs_not_visited.clear()
ucs_list = [Node(0)]
ucs_list.clear()
ucs_visited = [Node(0)]
ucs_visited.clear()

A_visited = [Node(0)]
A_visited.clear()
A_not_vistied = [Node(0)]
A_not_vistied.clear()

A_visited_manh = [Node(0)]
A_visited_manh.clear()
A_not_vistied_manh = [Node(0)]
A_not_vistied_manh.clear()

test = []


class SearchAlgorithms:
    ''' * DON'T change Class, Function or Parameters Names and Order
        * You can add ANY extra functions,
          classes you need as long as the main
          structure is left as is '''
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    totalCost = -1  # Represents the total cost in case using UCS, AStar (Euclidean or Manhattan)
    edges = []
    edgess = []

    def __init__(self, mazeStr, edgeCost=None):
        ''' mazeStr contains the full board
         The board is read row wise,
        the nodes are numbered 0-based starting
        the leftmost node'''
       # maze_list.clear()
        maze_list.clear()
        maze_nodes.clear()
        maze_nodes_2d.clear()
        self.path = []
        self.fullPath = []
        dfs_visited.clear()
        dfs_not_visited.clear()
        bfs_not_visited.clear()
        bfs_visited.clear()
        ucs_list.clear()
        ucs_visited.clear()
        self.edges.clear()
        self.edges = edgeCost
        A_visited.clear()
        A_not_vistied.clear()
        A_visited_manh.clear()
        A_not_vistied_manh.clear()
        self.edgess.clear()

        x = mazeStr.split(" ")
        row_num = len(x)

        for row in x:
            y = row.split(",")
            for n in y:
                maze_list.append(n)

        '''
        for i in range(len(x)):
            row = x[i]
            y = row.split(",")
            maze_list.append(y)
            '''

        self.col_num = int(len(maze_list) / row_num)
        self.rows = row_num
        total_num = len(maze_list)
        w = 1
        for d in range(0, total_num):
            self.edgess.append(w)
        for h in range(0, total_num):
            R = int(h / self.col_num)
            C = int((h % self.col_num))
            if maze_list[h] == 'E':
                rr = R
                cc = C
        for i in range(0, total_num):
            new_node = Node(maze_list[i])
            new_node.id = i
            r = int(i / self.col_num)
            c = int((i % self.col_num))
            f1 = (r - rr)
            f2 = (c - cc)
            d = abs(f1)
            g = abs(f2)
            if edgeCost is not None:
                new_node.edgeCost = 1000000
                # l goz2 bta3 l euldin
                f = 2
                total_under_the_root = (d ** f) + (g ** f)
                total_her_euclidean = math.sqrt(total_under_the_root)
                new_node.hOfN = total_her_euclidean

                # l goz2 bta3 l manhtan
            else:
                new_node.edgeCost = 1000000
                # new_node.edgeCost = 1
                total_her_manhattan = d + g
                new_node.hOfN = total_her_manhattan
            # r = int(i/self.col_num)
            # c = int((i % self.col_num))

            if maze_list[i] == 'S':
                self.start_ind = i
            elif maze_list[i] == 'E':
                self.end_ind = i

            if maze_list[i] != '#':
                if c == 0:
                    new_node.left = None
                    new_node.right = maze_list[i + 1]
                elif c == self.col_num - 1:
                    new_node.right = None
                    new_node.left = maze_list[i - 1]
                else:
                    new_node.right = maze_list[i + 1]
                    new_node.left = maze_list[i - 1]
                if r == 0:
                    new_node.up = None
                    new_node.down = maze_list[i + self.col_num]

                elif r == row_num - 1:
                    new_node.down = None
                    new_node.up = maze_list[i - self.col_num]
                else:
                    new_node.down = maze_list[i + self.col_num]
                    new_node.up = maze_list[i - self.col_num]
            maze_nodes.append(new_node)
        maze_nodes[self.start_ind].edgeCost = 0
        maze_nodes[self.start_ind].previousNode = self.start_ind

        cntr = 0
        tmp_list = [Node(0)]
        tmp_list.clear()
        for x in range(row_num):
            for y in range(self.col_num):
                tmp_list.append(maze_nodes[cntr])
                cntr = cntr + 1

            maze_nodes_2d.append(tmp_list)
            tmp_list = [Node(0)]
            tmp_list.clear()
        # print(maze_nodes[x].id)
        for x in range(row_num):
            for y in range(self.col_num):
                test = maze_nodes_2d[x][y]
                #print(test.id)
        row, col = self.to_2d_array(self.start_ind)
        dfs_not_visited.append(maze_nodes_2d[row][col])
        bfs_not_visited.append(maze_nodes_2d[row][col])
        ucs_list.append(maze_nodes_2d[row][col])
        # deh bta3t l Euclidean
        A_not_vistied.append(maze_nodes_2d[row][col])
        # deh bta3t l Manhattanan
        A_not_vistied_manh.append(maze_nodes_2d[row][col])

    def DFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        if len(dfs_not_visited) == 0:
            return self.path, self.fullPath
        if self.end_ind == dfs_not_visited[0].id:
            row, col = self.to_2d_array(self.end_ind)
            dfs_visited.append(maze_nodes_2d[row][col])
            # self.path_finder()
            self.full_path_finder()
            return self.path, self.fullPath

        if dfs_not_visited[0] not in dfs_visited:
            dfs_visited.append(dfs_not_visited[0])
            currentNode = dfs_not_visited[0]
            dfs_not_visited.pop(0)
            #maze_list[i][j].
            row, col = self.to_2d_array(currentNode.id + 1)
            if currentNode.right is not None and currentNode.right != '#':
                if maze_nodes_2d[row][col] not in dfs_not_visited:
                    if maze_nodes_2d[row][col] not in dfs_visited:
                        dfs_not_visited.insert(0, maze_nodes_2d[row][col])
                        maze_nodes_2d[row][col].previousNode = currentNode.id
            row, col = self.to_2d_array(currentNode.id - 1)
            if currentNode.left is not None and currentNode.left != '#':
                if maze_nodes_2d[row][col] not in dfs_not_visited:
                    if maze_nodes_2d[row][col] not in dfs_visited:
                        dfs_not_visited.insert(0, maze_nodes_2d[row][col])
                        maze_nodes_2d[row][col].previousNode = currentNode.id

            row, col = self.to_2d_array(currentNode.id + self.col_num)
            if currentNode.down is not None and currentNode.down != '#':
                if maze_nodes_2d[row][col] not in dfs_not_visited:
                    if maze_nodes_2d[row][col] not in dfs_visited:
                        dfs_not_visited.insert(0, maze_nodes_2d[row][col])
                        maze_nodes_2d[row][col].previousNode = currentNode.id
            row, col = self.to_2d_array(currentNode.id - self.col_num)
            if currentNode.up is not None and currentNode.up != '#':
                if maze_nodes_2d[row][col] not in dfs_not_visited:
                    if maze_nodes_2d[row][col] not in dfs_visited:
                        dfs_not_visited.insert(0, maze_nodes_2d[row][col])
                        maze_nodes_2d[row][col].previousNode = currentNode.id

            return self.DFS()
        # return self.path, self.fullPath

    def BFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        if len(bfs_not_visited) == 0:
            return self.path, self.fullpath
        if self.end_ind == bfs_not_visited[0].id:
            row, col = self.to_2d_array(self.end_ind)
            bfs_visited.append(maze_nodes_2d[row][col])
            # self.path_finder()
            self.full_path_finder()
            return self.path, self.fullPath
        if bfs_not_visited[0] not in bfs_visited:
            bfs_visited.append(bfs_not_visited[0])
            currentnode = bfs_not_visited[0]
            bfs_not_visited.pop(0)
            row, col = self.to_2d_array(currentnode.id - self.col_num)
            if currentnode.up is not None and currentnode.up != "#" and maze_nodes_2d[row][col] not in bfs_not_visited:
                if maze_nodes_2d[row][col] not in bfs_visited:
                    bfs_not_visited.append(maze_nodes_2d[row][col])
                    maze_nodes_2d[row][col].previousNode = currentnode.id
            row, col = self.to_2d_array(currentnode.id + self.col_num)
            if currentnode.down is not None and currentnode.down != "#" and maze_nodes_2d[row][col] not in bfs_not_visited:
                if maze_nodes_2d[row][col] not in bfs_visited:
                    bfs_not_visited.append(maze_nodes_2d[row][col])
                    maze_nodes_2d[row][col].previousNode = currentnode.id
            row, col = self.to_2d_array(currentnode.id - 1)
            if currentnode.left is not None and currentnode.left != "#" and maze_nodes_2d[row][col] not in bfs_not_visited:
                if maze_nodes_2d[row][col] not in bfs_visited:
                    bfs_not_visited.append(maze_nodes_2d[row][col])
                    maze_nodes_2d[row][col].previousNode = currentnode.id
            row, col = self.to_2d_array(currentnode.id + 1)
            if currentnode.right is not None and currentnode.right != "#" and maze_nodes_2d[row][col] not in bfs_not_visited:
                if maze_nodes_2d[row][col] not in bfs_visited:
                    bfs_not_visited.append(maze_nodes_2d[row][col])
                    maze_nodes_2d[row][col].previousNode = currentnode.id

            return self.BFS()

    def UCS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        '''maze_nodes.sort(key=lambda Node: Node.edgeCost, reverse=False)
        for x in maze_nodes:
            print(x.edgeCost)'''

        while len(ucs_list) != 0:
            ucs_list.sort(key=lambda Node: Node.edgeCost, reverse=False)

            current_node = ucs_list[0]
            ucs_list.pop(0)
            ucs_visited.append(current_node)
            if current_node.id == self.end_ind:
                self.totalCost = current_node.edgeCost
                self.ucs_full_path()
                return self.path, self.fullPath, self.totalCost
            y = current_node.edgeCost
            cost = current_node.edgeCost + y
            row, col = self.to_2d_array(current_node.id + 1)
            if current_node.right is not None and current_node.right != '#' and maze_nodes_2d[row][col] not in ucs_visited:
                if maze_nodes_2d[row][col].edgeCost >= y + self.edges[current_node.id + 1]:
                    maze_nodes_2d[row][col].edgeCost = y + self.edges[current_node.id + 1]
                    maze_nodes_2d[row][col].previousNode = current_node.id
                    ucs_list.append(maze_nodes_2d[row][col])
            row, col = self.to_2d_array(current_node.id - 1)
            if current_node.left is not None and current_node.left != '#' and maze_nodes_2d[row][col] not in ucs_visited:
                if maze_nodes_2d[row][col].edgeCost >= y + self.edges[current_node.id - 1]:
                    maze_nodes_2d[row][col].edgeCost = y + self.edges[current_node.id - 1]
                    maze_nodes_2d[row][col].previousNode = current_node.id
                    ucs_list.append(maze_nodes_2d[row][col])
            row, col = self.to_2d_array(current_node.id - self.col_num)
            if current_node.up is not None and current_node.up != '#' and maze_nodes_2d[row][col] not in ucs_visited:
                if maze_nodes_2d[row][col].edgeCost >= y + self.edges[current_node.id - self.col_num]:
                    maze_nodes_2d[row][col].edgeCost = y + self.edges[current_node.id - self.col_num]
                    maze_nodes_2d[row][col].previousNode = current_node.id
                    ucs_list.append(maze_nodes_2d[row][col])
            row, col = self.to_2d_array(current_node.id + self.col_num)
            if current_node.down is not None and current_node.down != '#' and maze_nodes_2d[row][col] not in ucs_visited:
                if maze_nodes_2d[row][col].edgeCost >= y + self.edges[current_node.id + self.col_num]:
                    maze_nodes_2d[row][col].edgeCost = y + self.edges[current_node.id + self.col_num]
                    maze_nodes_2d[row][col].previousNode = current_node.id
                    ucs_list.append(maze_nodes_2d[row][col])
        # return self.path, self.fullPath, self.totalCost

    def AStarEuclideanHeuristic(self):
        # Cost for a step is calculated based on edge cost of node
        # and use Euclidean Heuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        while len(A_not_vistied) != 0:
            A_not_vistied.sort(key=lambda Node: Node.heuristicFn, reverse=False)

            current_node = A_not_vistied[0]
            A_not_vistied.pop(0)
            A_visited.append(current_node)
            if current_node.id == self.end_ind:
                self.totalCost = float(current_node.heuristicFn)
                self.A_full_path()
                return self.path, self.fullPath, self.totalCost
            x = current_node.edgeCost
            row, col = self.to_2d_array(current_node.id + 1)
            if current_node.right is not None and current_node.right != '#' and maze_nodes_2d[row][col] not in A_visited:
                if maze_nodes_2d[row][col].edgeCost >= x + self.edges[current_node.id + 1]:
                    maze_nodes_2d[row][col].edgeCost = x + self.edges[current_node.id + 1]
                    maze_nodes_2d[row][col].previousNode = current_node.id
                    maze_nodes_2d[row][col].heuristicFn = maze_nodes_2d[row][col].edgeCost + maze_nodes_2d[row][col].hOfN
                    A_not_vistied.append(maze_nodes_2d[row][col])
            row, col = self.to_2d_array(current_node.id - 1)
            if current_node.left is not None and current_node.left != '#' and maze_nodes_2d[row][col] not in A_visited:
                if maze_nodes_2d[row][col].edgeCost >= x + self.edges[current_node.id - 1]:
                    maze_nodes_2d[row][col].edgeCost = x + self.edges[current_node.id - 1]
                    maze_nodes_2d[row][col].previousNode = current_node.id
                    maze_nodes_2d[row][col].heuristicFn = maze_nodes_2d[row][col].edgeCost + maze_nodes_2d[row][col].hOfN
                    A_not_vistied.append(maze_nodes_2d[row][col])
            row, col = self.to_2d_array(current_node.id - self.col_num)
            if current_node.up is not None and current_node.up != '#' and maze_nodes_2d[row][col] not in A_visited:
                if maze_nodes_2d[row][col].edgeCost >= x + self.edges[current_node.id - self.col_num]:
                    maze_nodes_2d[row][col].edgeCost = x + self.edges[current_node.id - self.col_num]
                    maze_nodes_2d[row][col].previousNode = current_node.id
                    maze_nodes_2d[row][col].heuristicFn = maze_nodes_2d[row][col].edgeCost + maze_nodes_2d[row][col].hOfN
                    A_not_vistied.append(maze_nodes_2d[row][col])
            row, col = self.to_2d_array(current_node.id + self.col_num)
            if current_node.down is not None and current_node.down != '#' and maze_nodes_2d[row][col] not in A_visited:
                if maze_nodes_2d[row][col].edgeCost >= x + self.edges[current_node.id + self.col_num]:
                    maze_nodes_2d[row][col].edgeCost = x + self.edges[current_node.id + self.col_num]
                    maze_nodes_2d[row][col].previousNode = current_node.id
                    maze_nodes_2d[row][col].heuristicFn = maze_nodes_2d[row][col].edgeCost + maze_nodes_2d[row][col].hOfN
                    A_not_vistied.append(maze_nodes_2d[row][col])

        # return self.path, self.fullPath, self.totalCost

    def AStarManhattanHeuristic(self):
        # Cost for a step is 1
        # and use ManhattanHeuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        # return self.path, self.fullPath, self.totalCost
        while len(A_not_vistied_manh) != 0:
            A_not_vistied_manh.sort(key=lambda Node: Node.heuristicFn, reverse=False)

            current_node = A_not_vistied_manh[0]
            A_not_vistied_manh.pop(0)
            A_visited_manh.append(current_node)
            if current_node.id == self.end_ind:
                self.totalCost = float(current_node.heuristicFn)
                self.Am_full_path()
                return self.path, self.fullPath, self.totalCost
            t = current_node.edgeCost
            row, col = self.to_2d_array(current_node.id - self.col_num)
            if current_node.up is not None and current_node.up != '#' and maze_nodes_2d[row][col] not in A_visited_manh:
                if maze_nodes_2d[row][col].edgeCost > t + self.edgess[current_node.id - self.col_num]:
                    maze_nodes_2d[row][col].edgeCost = t + self.edgess[current_node.id - self.col_num]
                    maze_nodes_2d[row][col].previousNode = current_node.id
                    maze_nodes_2d[row][col].heuristicFn = maze_nodes_2d[row][col].edgeCost + maze_nodes_2d[row][col].hOfN
                    A_not_vistied_manh.append(maze_nodes_2d[row][col])
            row, col = self.to_2d_array(current_node.id + self.col_num)
            if current_node.down is not None and current_node.down != '#' and maze_nodes_2d[row][col] not in A_visited_manh:
                if maze_nodes_2d[row][col].edgeCost > t + self.edgess[current_node.id + self.col_num]:
                    maze_nodes_2d[row][col].edgeCost = t + self.edgess[current_node.id + self.col_num]
                    maze_nodes_2d[row][col].previousNode = current_node.id
                    maze_nodes_2d[row][col].heuristicFn = maze_nodes_2d[row][col].edgeCost + maze_nodes_2d[row][col].hOfN
                    A_not_vistied_manh.append(maze_nodes_2d[row][col])
            row, col = self.to_2d_array(current_node.id - 1)
            if current_node.left is not None and current_node.left != '#' and maze_nodes_2d[row][col] not in A_visited_manh:
                if maze_nodes_2d[row][col].edgeCost > t + self.edgess[current_node.id - 1]:
                    maze_nodes_2d[row][col].edgeCost = t + self.edgess[current_node.id - 1]
                    maze_nodes_2d[row][col].previousNode = current_node.id
                    maze_nodes_2d[row][col].heuristicFn = maze_nodes_2d[row][col].edgeCost + maze_nodes_2d[row][col].hOfN
                    A_not_vistied_manh.append(maze_nodes_2d[row][col])
            row, col = self.to_2d_array(current_node.id + 1)
            if current_node.right is not None and current_node.right != '#' and maze_nodes_2d[row][col] not in A_visited_manh:
                if maze_nodes_2d[row][col].edgeCost > t + self.edgess[current_node.id + 1]:
                    maze_nodes_2d[row][col].edgeCost = t + self.edgess[current_node.id + 1]
                    maze_nodes_2d[row][col].previousNode = current_node.id
                    maze_nodes_2d[row][col].heuristicFn = maze_nodes_2d[row][col].edgeCost + maze_nodes_2d[row][col].hOfN
                    A_not_vistied_manh.append(maze_nodes_2d[row][col])

    def full_path_finder(self):
        temp_full_path = []
        for x in dfs_visited:
            temp_full_path.append(x.id)
        self.fullPath = temp_full_path
        for x in bfs_visited:
            temp_full_path.append(x.id)
        self.fullPath = temp_full_path


    def ucs_full_path(self):
        temp_full_path = []
        for x in ucs_visited:
            temp_full_path.append(x.id)
        self.fullPath = temp_full_path

    def A_full_path(self):
        temp_full_path = []
        for x in A_visited:
            temp_full_path.append(x.id)
        self.fullPath = temp_full_path

    def Am_full_path(self):
        temp_full_path = []
        for x in A_visited_manh:
            temp_full_path.append(x.id)
        self.fullPath = temp_full_path

    def path_finder(self):
        i = self.end_ind
        row, col = self.to_2d_array(i)
        self.path.append(maze_nodes_2d[row][col].id)
        while i != self.start_ind:
            self.path.append(maze_nodes_2d[row][col].previousNode)
            i = maze_nodes_2d[row][col].previousNode
            row, col = self.to_2d_array(i)
        self.path.reverse()

    def to_2d_array(self, index):
        row = int(index/self.col_num)
        col = int(index-(row*self.col_num))
        return row, col


def main():
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.DFS()
    print('**DFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')

    #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.BFS()
    print('**BFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')
    #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.',
                                  [0, 15, 2, 100, 60, 35, 30, 3
                                      , 100, 2, 15, 60, 100, 30, 2
                                      , 100, 2, 2, 2, 40, 30, 2, 2
                                      , 100, 100, 3, 15, 30, 100, 2
                                      , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.UCS()
    print('** UCS **\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\nTotal Cost: ' + str(
        TotalCost) + '\n\n')
    '''searchAlgo.UCS()
    print('Total Cost: ' + str(searchAlgo.totalCost) + '\n\n')'''
    #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.',
                                  [0, 15, 2, 100, 60, 35, 30, 3
                                      , 100, 2, 15, 60, 100, 30, 2
                                      , 100, 2, 2, 2, 40, 30, 2, 2
                                      , 100, 100, 3, 15, 30, 100, 2
                                      , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.AStarEuclideanHeuristic()
    print('**ASTAR with Euclidean Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')

    #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath, TotalCost = searchAlgo.AStarManhattanHeuristic()
    print('**ASTAR with Manhattan Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')


main()



