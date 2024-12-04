import re

def read_input():
    with open('input4.txt') as f:
        return f.readlines() 

def listToMatrix(lines):
    return [list(line) for line in lines]

def findXmas(strings):
    matches=[]
    for line in strings:
        matches.append(re.findall(r'XMAS|SAMX',line))
    return matches

def flatten_diagonally(matrix):
    diagonals = []
    for i in range(len(matrix) + len(matrix[0]) - 1):
        diagonal = []
        for j in range(max(0, i - len(matrix[0]) + 1), min(len(matrix), i + 1)):
            diagonal.append(matrix[j][i - j])
        diagonals.append(''.join(diagonal))
    return diagonals


def main():
    count=0
    lines = read_input()
    matrix = listToMatrix(lines)
    count+=len(findXmas(lines))
    print(count)
    
    column_strings = [''.join(row) for row in zip(*matrix)]
    #print(column_strings)
    count+=len(findXmas(column_strings))
    print(count)
    
    diagonal_strings = flatten_diagonally(matrix)
    count += len(findXmas(diagonal_strings))
    print(count)
    #print(listToMatrix(lines))
    

if __name__ == '__main__':
    main()