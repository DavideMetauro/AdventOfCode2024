clear=[]
quantity=[]
final=[]

def read_input():
    count = 0
    with open('input9_test.txt', 'r') as file:
        while True:
            c = file.read(1)
            if not c:
                break
            if count%2==0:
                quantity.append(int(c))
            else:
                clear.append(int(c))
            #print(c, end='')
            count+=1

def rearrange():
    for i in range(len(quantity)-1, 0, -1):
        for j in range(len(clear)):
            if quantity[i] <= clear[j] and quantity[i] != 0:
                clear_index=0
                for n in clear[0:j]:
                    clear_index+=n 
                for n in quantity[0:j+1]:
                    clear_index+=n
                quantity_index=final.index(i)

                for k in range(quantity[i]):
                    print(final[clear_index:].index(None))
                    final.pop(final[clear_index:].index(None) + clear_index)
                    final.insert(clear_index, i)
                    final.pop(final[quantity_index:].index(i) + quantity_index)
                    #final[quantity_index:].remove(i)
                    final.insert(quantity_index, None)
                    #final[quantity_index:].insert(0, None)
                clear[j] -= quantity[i]
                clear[i-1] += quantity[i]
                quantity[i] = 0
                break
        

def create_final():
    for i in range(len(quantity)-1):
        final.extend(i for j in range(quantity[i]))
        final.extend(None for j in range(clear[i]))
    final.extend(len(quantity)-1 for j in range(quantity[-1]))



def check_sum():
    return sum([i*final[i] for i in range(len(final)) if final[i] is not None])

if __name__ == "__main__":
    read_input()
    create_final()
    print(final)
    rearrange()
    print(final)
    print(check_sum())


