import re

def read_input():
    with open("input3.txt") as f:
        return f.read().replace('\n','*')
    
def find_instructions(data):
    instructions = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)',data)
    return instructions

def calculate_mul(instructions):
    sum=0
    enebled = True
    for instr in instructions:
        if instr == 'do()':
            enebled = True
        elif instr == 'don\'t()':
            enebled = False
        elif enebled:
            values = re.findall(r'\d+',instr)
            x, y = map(int,values)
            sum+=x*y
    return sum
    
def main():
    data = read_input()
    instructions=find_instructions(data)
    print(calculate_mul(instructions))

if __name__ == '__main__':
    main()
