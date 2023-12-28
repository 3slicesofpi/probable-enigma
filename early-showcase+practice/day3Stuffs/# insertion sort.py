# insertion sort
raw = [21,3,45,10]


def sortArea(array,key):
    done = False
    here = len(array)-1
    while (done != True):
        if here == -1:
            array.insert(0,key)
            done = True
        elif key >= array[here]:
            array.insert(here+1,key)
            done = True
        else:
            here -= 1
        
    return array
    
def insertionSort(raw):
    long = len(raw)
    for iters in range(long):
        raw = sortArea(raw[:iters],raw[iters]) + raw[(iters+1):] # <--- unsorted
    return raw

print(insertionSort(raw))
        