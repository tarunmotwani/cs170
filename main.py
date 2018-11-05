from heapq import heapify
from heapq import heappop
from heapq import heappush
import heapq
import copy
import queue
import time
goal = [[1,2,3], [4,5,6], [7,8,0]] #ideal state using a 3x3 matrix array

class Node:
    #state, heuristic, depth, and cost
    def __init__(self, current, heuristic, depth, cost):
        self.state = current                    #current state of this node
        self.heuristic = heuristic               #h(n)    heuristic is how far we're about to go to get to the goal state
        self.depth = depth                       #g(n) depth is how far we've traversed 
        self.cost = heuristic + depth            #h(n) + g(n) calculation of total moves altogether
    def __lt__(self, other):
        # if self.heuristic < other.heuristic: return self.heuristic < other.heuristic
        # return self.depth < other.depth
        return (self.cost > other.cost) - (self.cost < other.cost)  #0 mid
    #stackoverflow page https://stackoverflow.com/questions/47912064/typeerror-not-supported-between-instances-of-heapnode-and-heapnode
    
    # def getState(self, state):
    #     return self.state                        #function to return the current state of the node
    def operators(self, state):                  
        self.top = state                            #operators for puzzle options
        self.left = state
        self.right = state
        self.down = state
def getCost(node):
        return node.heuristic+node.depth
def expand(node):                              #passing in the current node value
    opArray = []                                    #empty operator list (saves possibilities)
    #steps
    #1)find the blank space
    curr = node.state                               #saving the current state for future reference
    i,j=findZero(node.state)                        #finding location of the empty space value
    depth = node.depth + 1                          #increment the depth every expansion
    #2)find the limitations of all the operations based on the board
    count = 0
    if i > 0:
        node.up = copy.deepcopy(curr)                   #https://stackoverflow.com/questions/17246693/what-exactly-is-the-difference-between-shallow-copy-deepcopy-and-normal-assignm
        node.up[i][j] = node.up[i-1][j]                 #replace with upper value
        node.up[i-1][j] = 0                               #original goes to zero
        opArray.append(Node(node.up, 0, depth, depth))                      #opArray holds operator state possibilities
        count += 1
    if i < 2:  #no down for row 2   
        node.down = copy.deepcopy(curr)
        node.down[i][j] = node.down[i+1][j]              #eliminates down operator for bottom row
        node.down[i+1][j] = 0
        opArray.append(Node(node.down,0, depth,depth ))
        count += 1
    if j > 0:  #no left                                                 #eliminaes left operator for left row
        node.left = copy.deepcopy(curr)                                 #copy state and all its attachments
        node.left[i][j] = node.left[i][j-1]                             #accessing column to left and assigning value...
        node.left[i][j-1] = 0                                           #orig goes to zero
        opArray.append(Node(node.left,0, depth,depth))                  #append new node
        count += 1
    if j < 2: #no right
        node.right = copy.deepcopy(curr)
        node.right[i][j] = node.right[i][j+1]
        node.right[i][j+1] = 0
        opArray.append(Node(node.right,0, depth, depth))
        count += 1
    print("Expanding state")
    #3)copy over the variables based on cheapest heuristics
    # print(opArray[1].state)
    # print('here is expansion')
    return opArray, count
def findZero(node):
    for i in range(3):                                          #in row 0-2
        for j in range(3):                                      #in column 0-2
            if node[i][j] == 0: return i,j                      #find zero and return it
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
    for i in range(3):                                      #in row
        for j in range(3):                                  #in column
            if puzzle[i][j] != goal[i][j]:                  #checking current vs goal to find tiles not matching the location they are supposed to be
                if puzzle[i][j] != 0: count += 1                               #inc count by 1
    return count
def queueing(x, queue, alg):
    arr = [1,2,3]
    # print("container ", x)
    for i in range(len(x)):                                         #access the current element of the list of options
        if alg == '1':
            x[i].heuristic = 0                                       #uniform cost search has no heuristic calculation
            # print('ucf h=', x[i].heuristic)
            
        if alg == '2':
            x[i].heuristic = misplacedTileHeuristic(x[i].state)     #mt heuristic calculation for each option
            # print('mt h=', x[i].heuristic)
        if alg == '3':
            x[i].heuristic = manhattanDistanceHeuristic(x[i].state) #md heuristic calculation for each option
        x[i].cost = getCost(x[i])                                   #cost function
        # print('md h=', x[i].heuristic
        heapq.heappush(queue, x[i])                                 #push to priority queue the best option
        
    # print('queueing' )
def display(x): 
    for i in range(3): print(x.state[i][0], x.state[i][1], x.state[i][2])   #prints the 3x3 matrix with row and column access of the current state

def emptyCheck(node, temp):
    # if(node.state == temp.state):   #if the previous matches the original we exit
    #     print('invalid puzzle')
    #     exit(1)
    if(node.depth > 1000): 
        print('invalid puzzle')
        exit(1)

def goalCheck(node, numMax, numExpanded, start_time):
    # numExpanded, numMax = 0,0
    if node.state == goal:
        print('Goal!! \nTo solve this problem the search algorithm expanded a total of', numExpanded, ' nodes')
        print('The maximum number of nodes in the queue at any one time was', numMax)
        print('The depth of the goal node was ', node.depth)
        print("--- %s seconds ---" % (time.time() - start_time))
        exit(0)
    else: return False

def search(puzzle, alg):    # for i in range(len(x)):
    start_time = time.time()
    numMax, numExpanded = 0,0
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
    
    heap = []                                              #empty queue of nodes
    heapq.heappush(heap, node)                             #using a heap priority queue to always know the first element
    heapq.heapify(heap)
    # print("nodecheck ", queue)
    # heapq.heappush(queue, node)                             #using a heap priority queue to always know the first element
    # print("nodecheck 2", queue)
    flag = False
    count = 0
    goalState = False
    while goalState == False:                               #while loop for false
        key = heap[0]
        display(key)
        if flag == True:
            emptyCheck(key, heap[1])
        # print(count)
        if len(heap) > numMax: 
            numMax = len(heap)
        # print("maxupdate")
        goalState = goalCheck(key, numMax, numExpanded, start_time)
        heapq.heapify(heap)
        print('the best state to expand with a g(n) of', key.depth, 'and a f(n) of' , key.heuristic)   #printing the best solution
        current = heappop(heap)                                       #using a temp value to save the current state of the queue
        # print('expanding state')
        # for i in range(len(queue)): print("nodecheck inside",count,":", queue[i].state)
        x, numExpanded = expand(current)                                     #passing in the current node
        numExpanded += count 
        queueing(x, heap, alg)
        # if count == 10: break
        # for i in range(len(queue)): print(queue[i].heuristic)
        flag = True

def cases():
    # puzzle = [[1,2,3], [4,5,6], [7,8,0]] #trivial solution
    # puzzle = [[1,2,3], [4,5,6], [7,0,8]] #veryEasy solution
    # puzzle = [[1,2,0], [4,5,3], [7,8,6]] #easy solution
    # puzzle = [[0,1,2], [4,5,3], [7,8,6]] #doable solution
    # puzzle = [[8,7,1], [6,0,2], [8,7,1]] #ohboy solution
    # puzzle = [[1,2,3], [4,5,6], [8,7,0]] #impossible solution
    puzzle = [[1,2,3], [4,8,0], [7,6,5]] #custom solution
    return puzzle

if __name__ == '__main__':
    puzzle = []
    puzzle = cases()
    print('Welcome to 8-puzzle!')
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
    else:
        print('invalid choice try again')
   
