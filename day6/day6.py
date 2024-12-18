def read_input():
    with open("input6.txt") as f:
        return [line.strip() for line in f.readlines()]
    
def find_start(lines):
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in ['^', '<', '>', 'v']:
                return (i, j, char)
            
def move(x, y, direction, lines):
    directions = ['^', '>', 'v', '<']
    if lines[x][y]=='#':
        direction = directions[(directions.index(direction)+1)%4]
    else:
        lines[x][y] = 'X'
    if direction == '^':
        return (x-1, y)
    elif direction == '<':
        return (x, y-1)
    elif direction == '>':
        return (x, y+1)
    elif direction == 'v':
        return (x+1, y)
    
def main():
    lines = read_input()
    directions = ['^', '<', '>', 'v']
    print(lines)
    startX, startY, startDir = find_start(lines)

if __name__ == "__main__":
    main()