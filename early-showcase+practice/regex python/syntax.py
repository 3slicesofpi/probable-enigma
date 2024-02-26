import re
from random import randint
print(re.findall('[a-zA-Z]','gEt cLiPPeD b0zo !1!!1l!!'))
print(re.findall('[0-9]','147.7862.4571.0364'))
print(re.findall('[0-'+str(randint(1,9))+']','1124646992y3y59p'))

list0 = []
for elements in re.split('\s','cat fat rat ate! rag ack! tack nag lack black'):
    list0.append(re.search('(.at|^.?ack)[!?,.*]{0}$',elements))
    if list0[-1] != None:
        list0[-1] = list0[-1].string
    else:
        list0.remove(list0[-1])
print(list0)

word0 = re.search('\AThe','The box is grey.')
if word0 != None:
    print(word0.string)
else:
    print(None)



    