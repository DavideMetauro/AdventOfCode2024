def read_input():
    with open("input6.txt") as f:
        return [line.strip() for line in f.readlines()]
    
def find_start(lines):
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in ['^', '<', '>', 'v']:
                return (i, j, char)
            
def move(x, y, direction, matrix):
    directions = ['^', '>', 'v', '<']
    if matrix[x][y]=='#':
        direction = directions[(directions.index(direction)+1)%4]
    else:
        matrix[x][y] = 'X'
    if direction == '^':
        return (x-1, y, direction)
    elif direction == '<':
        return (x, y-1, direction)
    elif direction == '>':
        return (x, y+1, direction)
    elif direction == 'v':
        return (x+1, y, direction)
    
def main():
    lines = read_input()
    matrix = [list(line.strip()) for line in lines]
    directions = ['^', '<', '>', 'v']
    x, y, dir = find_start(matrix)
    while x>=0 and x<len(matrix) and y>=0 and y<len(matrix[0]):
        x, y, dir = move(x, y, dir, matrix)
    count_x = sum(line.count('X') for line in matrix)
    print(f"Total X count: {count_x}")

if __name__ == "__main__":
    main()