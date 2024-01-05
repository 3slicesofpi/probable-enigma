raw = [2,3,4,6,6,8,9]

def dblRmv(raw):
    raw = sorted(raw)
    iterate = 0
    while iterate != len(raw)-1: # the vars should converge 
        # yes len(raw) is a var, not a const
        if raw[iterate] == raw[iterate+1]:
            raw.remove(raw[iterate+1])
        else:
            iterate += 1
    return raw

print(dblRmv(raw))