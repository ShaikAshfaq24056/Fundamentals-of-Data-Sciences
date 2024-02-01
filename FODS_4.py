import numpy as np
data=np.array([10000,20000,25000,30000])
total=np.sum(data)
print(total)
q1=data[0]
q4=data[-1]
per=((q4-q1)/q1)*100
print(per)
