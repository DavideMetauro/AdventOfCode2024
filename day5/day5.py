#setX
#setY
#map(num, countNum)
#index[len(setX)]
with open('input5.txt', 'r') as file:
    input_data = file.read().split('\n\n')
    part1 = input_data[0].strip().split()
    part2 = input_data[1].strip().split(',')

setX = set()
setY = set()
map_num_count = {}

for pair in part1:
    num1, num2 = map(int, pair.split('|'))
    setX.add(num1)
    setY.add(num2)
    
print(setX)