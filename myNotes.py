
#timeit for loop
$ python3 -m timeit -s "import numpy" "arr = numpy.arange(1000)" "dif = numpy.zeros(999,int)" "for i in range (1, len(arr)): dif[i-1] = arr[i] - arr[i-1]"
