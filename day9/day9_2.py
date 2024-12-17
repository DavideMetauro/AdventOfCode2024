free_spaces=[]
occupied_spaces=[]
final=[]

def read_input():
    count = 0
    with open('input9.txt', 'r') as file:
        while True:
            c = file.read(1)
            if not c:
                break
            if count%2==0:
                occupied_spaces.append(int(c))
            else:
                free_spaces.append(int(c))
            count+=1

def count_clear(last_i):
    index=0
    free_dict = {}
    for i in range(last_i):
        if final[i] is None and final[i-1] is not None:
            index = i
            if index in free_dict:
                free_dict[index] += 1
            else:
                free_dict[index] = 1
        elif final[i] is None and final[i-1] is None:
            free_dict[index] += 1
    return free_dict


def create_final():
    for i in range(len(occupied_spaces)-1):
        final.extend(i for j in range(occupied_spaces[i]))
        final.extend(None for j in range(free_spaces[i]))
    final.extend(len(occupied_spaces)-1 for j in range(occupied_spaces[-1]))

def rearrange():
    for i in range(len(occupied_spaces)-1,0,-1):
        free_dict = count_clear(final.index(i))
        for key in free_dict:
            if free_dict[key] >= occupied_spaces[i]:
                remove_index = final.index(i)
                for j in range(occupied_spaces[i]):
                    final[key+j] = i
                    removed=final.pop(remove_index)

                for j in range(occupied_spaces[i]):
                    final.insert(remove_index,None)
                    
                break
                
        

def check_sum():
    return sum([i*final[i] for i in range(len(final)) if final[i] is not None])

if __name__ == "__main__":
    read_input()
    create_final()
    rearrange()
    #rint(final)
    print(check_sum())


