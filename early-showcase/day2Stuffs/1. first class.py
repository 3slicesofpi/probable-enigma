# first class

class id():
    name = ""
    age = 0
    height = 0
    weight = 0


guy0 = id()

guy0.name = 'John'
guy0.age = 32
guy0.height = 180
guy0.weight = 57

guy1 = id()

guy1.name = 'Bob'
guy1.age = 19
guy1.height = 132
guy1.weight = 49

guy2 = id()

guys = [guy0,guy1,guy2]
print(guys[1].weight)

