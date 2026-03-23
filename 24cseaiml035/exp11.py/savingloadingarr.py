import numpy as np
arr=np.array([1,2,3,4])
np.save('my_array',arr)
loaded_arr=np.load('my_array,np')
print("loaded array:",loaded_arr)
