raw = [-7,-89,100,0]

def negHandler(raw,negOffset):
    long = len(raw)
    
    for here in range(long):
        if raw[here] < 0:
            negOffset += -raw[here]
    for here in range(long):
        raw[here] += negOffset
    return negOffset

negOffset = negHandler(raw,0)

final = ""
for target in raw:
    final = (final + " " + str(target)) # additional load burden

print(final + " with offset of " + str(negOffset))
