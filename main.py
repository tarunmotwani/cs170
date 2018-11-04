from heapq import heapify, heappop, heappush
import heapq
goal = [[1,2,3], [4,5,6], [7,8,0]] #ideal state

class Node:
    #state, heuristic, depth, and cost
    def __init__(self, current, heuristic, depth, cost):
        self.state = current                    #current state of this node
        self.heuristic = heuristic               #h(n)    heuristic is how far we're about to go to get to the goal state
        self.depth = depth                       #g(n) depth is how far we've traversed 
        self.cost = heuristic + depth            #h(n) + g(n) calculation of total moves altogether
    def getState(self, state):
        return self.state                        #function to return the current state of the node
    def operators(self, state):                  
        self.top = state
        self.left = state
        self.right = state
        self.down = state
        return []

def expand(node):                              #passing in the current node value
    opArray = []
    #steps
    #1)find the blank space
    i,j=findZero(node.state)
    #2)find the limitations by up, down left right operations based on the board
    
    if i != 0: #up not given option to expand
        node.up = node.state
        opArray.append(node.up)
    if i != 2:  #no down 
        node.down = node.state
        opArray.append(node.up)
    if j != 0:  #no left 
        node.left = node.state
        opArray.append(node.up)
    if j != 2: #no right
        node.right = node.state
        opArray.append(node.up)
    print(opArray)

    

    #3)copy over the variables based on cheapest heuristics

    

    print('here is expansion')
    return []
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
    for i in range(len(x)):
        if alg == arr[i]: 
            x[i].heuristic = 0
        elif alg == arr[i]: 
            x[i].heuristic = misplacedTileHeuristic(x[i])
        elif alg == arr[i]: 
            x[i].heuristic = manhattanDistanceHeuristic(x[i])
        heappush(queue, x[i])
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

def search(puzzle, alg):
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
    goalState = False
    while goalState == False:                               #while loop for false
        print('expanding state')
        display(node)
        emptyCheck(node)
        goalState = goalCheck(node, goalState)
        temp = heappop(queue)                                       #using a temp value to save the current state of the queue
        print('the best state to expand with a g(n) of ', node.depth, 'and a f(n) of ' , node.heuristic)   #printing the best solution
        print('expanding node')
        x = expand(temp)                                     #passing in the current node 
        # queueing(x, queue,alg)
        
        # print(x.state)
        goalState = True

# queueing function

# empty function
#goal state function

def cases():
    # puzzle = [[1,2,3], [4,5,6], [7,8,0]] #trivial solution
    # puzzle = [[1,2,3], [4,5,6], [7,0,8]] #veryEasy solution
    # puzzle = [[1,2,0], [4,5,3], [7,8,6]] #easy solution
    # puzzle = [[0,1,2], [4,5,3], [7,8,6]] #doable solution
    puzzle = [[8,7,1], [6,0,2], [8,7,1]] #ohboy solution
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