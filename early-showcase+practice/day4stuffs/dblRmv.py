
raw = [2,2,2,4,5,7,8,8,9,11]

# needs a sorted list
# readable version

def dblRmv(raw):
    raw = sorted(raw)
    long = 0
    iterate = 0
    result = [raw[0]]
    while len(raw) > long:
        if result[iterate] != raw[long]:
            result.append(raw[long])
            iterate += 1
        else:
            pass
        long += 1
    return result


print(dblRmv(raw))