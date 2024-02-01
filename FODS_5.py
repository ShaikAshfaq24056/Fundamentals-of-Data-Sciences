import numpy as np
fuel_efficiency=np.array([20,30,40,23])
avg=np.mean(fuel_efficiency)
print(avg)
car1=fuel_efficiency[0]
car2=fuel_efficiency[2]
per=((car2-car1)/car1)*100
print(per)
