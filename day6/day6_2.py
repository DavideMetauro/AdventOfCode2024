directions = ['^', '>', 'v', '<']
matrix=[]
def read_input():
    with open("input6.txt") as f:
        return [line.strip() for line in f.readlines()]
    
def find_start(lines):
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in ['^', '<', '>', 'v']:
                return (i, j, char)
            
def move(x, y, direction):

    if direction == '^':
        x_new, y_new=x-1, y
    elif direction == '<':
        x_new, y_new=x, y-1
    elif direction == '>':
        x_new, y_new=x, y+1
    elif direction == 'v':
        x_new, y_new=x+1, y
    
    if not(x_new<0 or x_new>=len(matrix) or y_new<0 or y_new>=len(matrix[0])):
        if matrix[x_new][y_new] == '#':
            return x, y, directions[(directions.index(direction)+1)%4]
        else:
            matrix[x_new][y_new] = 'X'
            return x_new, y_new, direction
    else: 
        return None, None, None
    
def main():
    count_loop = 0
    lines = read_input()
    set_of_visited = set()
    global matrix
    matrix = [list(line.strip()) for line in lines]
    x_start, y_start, dir_start = find_start(matrix)
    matrix[x_start][y_start] = 'X'
    for i in range(len(matrix)) :
        for j in range(len(matrix[0])) :
            if matrix[i][j] == '#':
                continue
            if i == x_start and j == y_start:
                continue
            set_of_visited.clear()
            e_old = matrix[i][j]
            matrix[i][j]='#' 
            x, y, dir = x_start, y_start, dir_start
            while x is not None or y is not None or dir is not None:
                x,y,dir=move(x, y, dir)
                if (x, y, dir) in set_of_visited:
                    count_loop += 1
                    break
                else:
                    set_of_visited.add((x, y, dir))
            matrix[i][j]=e_old
            #print(len(set_of_visited))
    print(count_loop)

if __name__ == "__main__":
    main()