import numpy as np

arlist = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
        [13,14,15,16]]

arbitraryarray = np.array(arlist,float)

print("Array: {}".format(arbitraryarray))

secondrow = arbitraryarray[1,:]

print("number one: {}".format(secondrow))

thirdcolumn = arbitraryarray[:,2]

print("number two: {}".format(thirdcolumn))

arbitraryarray[1,1] = 0.21

print("number three: {}".format(arbitraryarray))

checkzeros = np.zeros([8,8])


print("number four: {}".format(checkzeros))

checkzeros[::2,::2] =1
print("number four: {}".format(checkzeros))
checkzeros[1::2,1::2] =1
print("number four: {}".format(checkzeros))
