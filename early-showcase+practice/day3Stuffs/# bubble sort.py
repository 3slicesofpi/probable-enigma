raw = [440, -203, 492, -596, -992, -193, 793, 441, -68, 706, 823, 76, -862, -691, 188, -908, 984, 392, 693, -940, 732, 646, -115, 384, -698, 841, 267, -404, -228, -171, 824, 264, -487, 363, -532, -160, -450, 929, -890, 116, -657, -907, 206, -120, 341, 140, -210, -194, -571, 826, 886, 464, 908, 490, 10, 90, 357, 64, -736, 242, 43, 541, 784, -78, 900, 514, 401, -359, -562, 47, -482, -653, -518, -536, 30, -713, 757, -851, 724, -565, -415, 182, -871, 902, 586, -285, -965, 422, 417, 754, -294, -116, -683, 806, -648, 509, -276, -645, -173, 526]

# raw = [92, 12, 41, 69]

def bubbleSort(raw):
    long = len(raw)
    for target in range(long-1):
        for compare in range(0, (long - target - 1)):
            if raw[compare] > raw[compare+1]:
                (raw[compare],raw[compare+1]) = (raw[compare+1],raw[compare])
        


bubbleSort(raw)

final = ""
for target in raw:
    final = (final + " " + str(target)) # additional load burden
print(str(final))

# problems: even bubbles not sorted.