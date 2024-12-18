directions = ['^', '>', 'v', '<']
def read_input():
    with open("input6.txt") as f:
        return [line.strip() for line in f.readlines()]
    
def find_start(lines):
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in ['^', '<', '>', 'v']:
                return (i, j, char)
            
def move(x, y, direction, matrix):
    
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
            move( x, y, directions[(directions.index(direction)+1)%4], matrix)
        else:
            matrix[x_new][y_new] = 'X'
            move( x_new, y_new, direction, matrix)
        return
    else: 
        return 
    
def main():
    lines = read_input()
    matrix = [list(line.strip()) for line in lines]
    x, y, dir = find_start(matrix)
    matrix[x][y] = 'X'
    move(x, y, dir, matrix)
    count_x = sum(line.count('X') for line in matrix)
    print("\n".join("".join(line) for line in matrix))
    print(f"Total X count: {count_x}")

if __name__ == "__main__":
    main()