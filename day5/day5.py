#setX
#setY
#map(num, countNum)
#index[len(setX)]
def read_input():
    with open('input5.txt', 'r') as file:
        input_data = file.read().split('\n\n')
        part1 = input_data[0].strip().split()
        part2 = input_data[1].strip().split(',')
    return part1, part2

def create_sets(part1):
    setX = set()
    setY = set()

    for pair in part1:
        num1, num2 = map(int, pair.split('|'))
        setX.add(num1)
        setY.add(num2)
        
    print(setX)
    print(setY)
    return setX, setY

def create_map(part2, setX, setY):
    map_num_count = {}

if __name__ == '__main__':
    part1, part2 = read_input()
    setX, setY = create_sets(part1)
    create_map(part2, setX, setY)