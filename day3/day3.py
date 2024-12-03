import re

def read_input():
    with open('input3.txt') as f:
        return f.read().replace('\n','*')
    
def find_mul(data):
    values = re.findall(r'mul\((\d+),(\d+)\)',data)
    return values

def calculate_mul(values):
    sum=0
    for value in values:
        #x, y = int(value[0]), int(value[1])
        x, y = map(int,value)
        sum+=x*y
    return sum
    
def main():
    data = read_input()
    values=find_mul(data)
    print(calculate_mul(values))

if __name__ == '__main__':
    main()