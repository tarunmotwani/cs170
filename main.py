from heapq import heapify, heappop, heappush
import heapq
import copy
goal = [[1,2,3], [4,5,6], [7,8,0]] #ideal state

class Node:
    #state, heuristic, depth, and cost
    def __init__(self, current, heuristic, depth, cost):
        self.state = current                    #current state of this node
        self.heuristic = heuristic               #h(n)    heuristic is how far we're about to go to get to the goal state
        self.depth = depth                       #g(n) depth is how far we've traversed 
        self.cost = heuristic + depth            #h(n) + g(n) calculation of total moves altogether
    def __lt__(self, other):
        return self.heuristic < other.heuristic
    #stackoverflow page https://stackoverflow.com/questions/47912064/typeerror-not-supported-between-instances-of-heapnode-and-heapnode
    
    # def getState(self, state):
    #     return self.state                        #function to return the current state of the node
    # def operators(self, state):                  
    #     self.top = state
    #     self.left = state
    #     self.right = state
    #     self.down = state
    #     return []

def expand(node):                              #passing in the current node value
    opArray = []
    #steps
    #1)find the blank space
    
    i,j=findZero(node.state)
    d = node.depth + 1
    #2)find the limitations by up, down left right operations based on the board
    
    # if i != 0:
    #     top = copy.deepcopy(node.state)
    #     top[i][j] = top[i-1][j]
    #     top[i-1][j] = 0
    #     opArray.append(top)
 
 
 #incorrect code
 #_______________________________________________________________________________
    if i != 0: #row 0 not given option to expand
        top = copy.deepcopy(node.state)
        top[i][j] = top[i-1][j]
        top[i-1][j] = 0
        topNode = Node(top,0, d, d)
        opArray.append(topNode)
    if i != 2:  #no down for row 2 
        down = copy.deepcopy(node.state)
        down[i][j] = down[i+1][j]
        down[i+1][j] = 0
        downNode = Node(down,0, d, d)
        opArray.append(downNode)
    if j != 0:  #no left 
        left = copy.deepcopy(node.state)
        left[i][j] = left[i][j-1]
        left[i][j-1] = 0
        leftNode = Node(left,0, d, d)
        opArray.append(leftNode)
    if j != 2: #no right
        right = copy.deepcopy(node.state)
        right[i][j] = right[i][j+1]
        right[i][j+1] = 0
        rightNode = Node(right,0, d, d)
        opArray.append(rightNode)
    # print(opArray)
#____________________________________________________________________________________
    

    #3)copy over the variables based on cheapest heuristics

    
    # print(opArray[1].state)
    print('here is expansion')
    return opArray
def findZero(node):
    for i in range(3): 
        for j in range(3): 
            if node[i][j] == 0: return i,j
def manhattanDistanceHeuristic(puzzle):
    result = 0
    for i in range(3):
        for j in range(3):                                                              #in i,j puzzle
            if puzzle[i][j] != goal[i][j]:
                for x in range(3):
                    for y in range(3):                                                  #check x,y goal
                        if puzzle[i][j] == goal[x][y]:                                  #if match
                            if puzzle[i][j] != 0: result += abs(x-i)+abs(y-j)           #not zero empty tile #sum absolute values of the difference
    return result                                                                       #return result       
def misplacedTileHeuristic(puzzle):                         
    count = 0                                       
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != goal[i][j]:                  #checking current vs goal to find misplaced tiles
                if puzzle[i][j] != 0: count += 1                               #inc count by 1
    return count
def queueing(x, queue, alg):
    arr = [1,2,3]
    # print("container ", x)
    for i in range(len(x)):
    #     if alg == arr[i]: 
    #         x[i].heuristic = 0
    #     elif alg == arr[i]: 
    #         x[i].heuristic = misplacedTileHeuristic(x[i])
    #     elif alg == arr[i]: 
    #         x[i].heuristic = manhattanDistanceHeuristic(x[i])
    #         print("manhattan heuristic test ", x[i])
        
        if alg == '1':
            x[i].heuristic = 0
            print('ucf h=', x[i].heuristic)
        if alg == '2':
            x[i].heuristic = misplacedTileHeuristic(x[i].state)
            print('mt h=', x[i].heuristic)
        if alg == '3':
            x[i].heuristic = manhattanDistanceHeuristic(x[i].state)
        print('md h=', x[i].heuristic)
        # print(x[i])
        # print("before",queue)
        heapq.heappush(queue, x[i])
    # print("after ",queue)
        
    print('queueing' )
def display(x): 
    for i in range(3): print(x.state[i][0], x.state[i][1], x.state[i][2])

def emptyCheck(node):
    if(node.state == []):
            print('empty fail')
            exit(1)

def goalCheck(node, goalState):
    numExpanded, numMax = 0,0
    if node.state == goal:
            print('Goal!! \n To solve this problem the search algorithm expanded a total of', numExpanded, ' nodes')
            print('The maximum number of nodes in the queue at any one time was', numMax)
            print('.\n The depth of the goal node was ', node.depth)
            return True
    else: return False

def search(puzzle, alg):    # for i in range(len(x)):
    #     if alg == arr[i]: 
    #         x[i].heuristic = 0
    #     elif alg == arr[i]: 
    #         x[i].heuristic = misplacedTileHeuristic(x[i])
    #     elif alg == arr[i]: 
    #         x[i].heuristic = manhattanDistanceHeuristic(x[i])
    #         print("manhattan heuristic test ", x[i])
    if alg == '1':
        heuristic = 0                                       #heuristic is zero
        node = Node(puzzle, 0, 0, 0)
        print(heuristic)
    elif alg == '2':
        heuristic = misplacedTileHeuristic(puzzle)          #calculate missingtile heuristic
        node = Node(puzzle, heuristic, 0, heuristic)        #pass in for initial node
        print(heuristic)                                    
    elif alg == '3':
        heuristic = manhattanDistanceHeuristic(puzzle)      #calculate manhattan heuristic
        node = Node(puzzle, heuristic, 0, heuristic)        #pass in for initial node
        print(heuristic)
    
    queue = []                                              #empty queue of nodes
    heapq.heappush(queue, node)                             #using a heap priority queue to always know the first element
    print("nodecheck ", queue)
    # heapq.heappush(queue, node)                             #using a heap priority queue to always know the first element
    # print("nodecheck 2", queue)
    # count = 0
    goalState = False
    while goalState == False:                               #while loop for false
        display(queue[0])
        emptyCheck(node)
        goalState = goalCheck(queue[0], goalState)
        heapify(queue)
        temp = heappop(queue)                                       #using a temp value to save the current state of the queue
        print('the best state to expand with a g(n) of ', temp.depth, 'and a f(n) of ' , temp.heuristic)   #printing the best solution
        print('expanding state')
        # for i in range(len(queue)): print("nodecheck inside",count,":", queue[i].state)
        x = expand(temp)                                     #passing in the current node 
        queueing(x, queue, alg)
        # count += 1
        # if count == 6: break


# queueing function

# empty function
#goal state function

def cases():
    # puzzle = [[1,2,3], [4,5,6], [7,8,0]] #trivial solution
    # puzzle = [[1,2,3], [4,5,6], [7,0,8]] #veryEasy solution
    # puzzle = [[1,2,0], [4,5,3], [7,8,6]] #easy solution
    puzzle = [[0,1,2], [4,5,3], [7,8,6]] #doable solution
    # puzzle = [[8,7,1], [6,0,2], [8,7,1]] #ohboy solution
    # puzzle = [[1,2,3], [4,5,6], [8,7,0]] #impossible solution
    # puzzle = [[3,2,8],[4,5,6],[0,1,7]] #custom solution
    return puzzle


if __name__ == '__main__':
    # puzzle = [[1,2,3], [4,8,0], [7,6,5]]
    # puzzle = [[3,2,8],[4,5,6],[0,1,7]]
    # puzzle = [[1,2,3], [4,5,6], [7,8,0]] #trivial solution
    puzzle = []
    puzzle = cases()

    print ('Type “1” to use a default puzzle, or “2” to enter your own puzzle.')
    choice = input()
    if choice == '1': 
        print('puzzle: ')
        print(puzzle)
    if choice == '2':
        print ('Enter your puzzle, use a zero to represent the blank \n ')
        arr = ['first', 'second', 'third']
        for i in range(3): 
            print ('Enter the ' + arr[i] + ' row, use space or tabs between numbers ')
            a,b,c = input().split()
            row = [a,b,c]
            for j in range(3): puzzle[i][j] = int(row[j])
        print(puzzle)
    print('Enter your choice of algorithm \n 1. Uniform Cost Search \n 2. A* with the Misplaced Tile heuristic. \n 3. A* with the Manhattan distance heuristic.')
    alg = input()
    if alg == '1':
        print('uniform cost search')
        search(puzzle, alg)
    if alg == '2':
        print('misplaced tile heuristic')
        search(puzzle, alg)
    if alg == '3':
        print('manhattan distance heuristic')
        search(puzzle, alg)
    
    
    # goal line text
    # if success == true
    #     print('Goal!! \n To solve this problem the search algorithm expanded a total of 123 nodes. \n The maximum number of nodes in the queue at any one time was 45. \n The depth of the goal node was 5')