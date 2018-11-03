import numpy as np

x = [x*0.005 for x in range(0,200)]
file = open('data1.txt','w')
for i in range(len(x)):
    file.write(
        str(x[i]) + '\n'
    )
file.close()