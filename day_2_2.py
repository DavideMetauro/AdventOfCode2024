with open('input_2.txt', 'r') as file:
    lines = file.readlines() 

data = [[int(num) for num in line.strip().split()] for line in lines]

safe = True
count = 0
for record in data:
    safe = True
    
    for i in range(len(record)):
        record_combined=record[:i]+record[i+1:]
        safe = True
        if not(record_combined == sorted(record_combined) or record_combined == sorted(record_combined, reverse=True)):
            safe = False
        else:
            for i in range(len(record_combined) - 1):
                if abs(record_combined[i] - record_combined[i + 1]) > 3 or abs(record_combined[i] - record_combined[i + 1]) == 0:
                    safe = False
                    break
        if safe:
            count+=1
            break
        

print(count)