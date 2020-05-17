import numpy as np

pList = [1, 2, 0.5]
randomarray = np.array(pList)

print('number one: {}'.format(randomarray))

arraystartstopinterval = np.arange(-2.0,2.0,0.2)

print('number two: {}'.format(arraystartstopinterval))

arrayequallyspaced = np.linspace(0.1,1.5,11)

print('number three: {}'.format(arrayequallyspaced))

onestring='ANBGFJFHDNDKD'
stringarray=np.array(onestring,dtype='c')
print('number four: {}'.format(stringarray))
