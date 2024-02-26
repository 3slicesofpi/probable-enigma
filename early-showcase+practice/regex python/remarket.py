import re
# example command
clientInput = 'lcndoqwnc,k,5'
clientCommand = None
clientArg0 = None
clientArg1 = None
# command:t, arg0:9, arg1:2


# split
clientInput = re.split(',',clientInput)
clientCommand = re.findall('^(t|r|b|p|v|e)',clientInput[0])
print(clientInput)
if len(clientInput) == 2:
    clientArg0 = re.findall('[0-9]',clientInput[1])
elif len(clientInput) == 3:
    clientArg1 = re.findall('[0-9]',clientInput[2])

print(clientCommand,clientArg0,clientArg1)