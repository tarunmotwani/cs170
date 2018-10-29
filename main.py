goal = [[1,2,3], [4,5,6], [7,8,0]]



# def search(puzzle, alg):
#     if alg == '1':




#uniform heuristic = 0
#misplaced time = 


if __name__ == '__main__':
    puzzle = [[1,2,3], [4,8,0], [7,6,5]]
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
        # search(puzzle, alg)
    if alg == '2':
        print('misplaced tile heuristic')
        # search(puzzle, alg)
    if alg == '3':
        print('manhattan distance heuristic')
        # search(puzzle, alg)
    
    # goal line text
    # if success == true
    #     print('Goal!! \n To solve this problem the search algorithm expanded a total of 123 nodes. \n The maximum number of nodes in the queue at any one time was 45. \n The depth of the goal node was 5')