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

def main():
    count=0
    lines = read_input()
    count+=len(findXmas(lines))
    print(count)
    column_strings = [''.join(row) for row in zip(*listToMatrix(lines))]
    #print(column_strings)
    count+=len(findXmas(column_strings))
    print(count)
    #print(listToMatrix(lines))
    

if __name__ == '__main__':
    main()