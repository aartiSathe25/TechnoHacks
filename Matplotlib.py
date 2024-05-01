import matplotlib.pyplot as plt
import numpy as np

years = [2001,2002,2003,2004,2005,2006,2007,2008]

gdp = [300.2,105.2,50.8,89.2,69,56,78,9]

plt.plot(years,gdp)

#plt.show()


arr = np.array([1,2,3,4,5])

arr1 = np.array(42)
print(arr)
print(type(arr))

#0D Array
print(np.array(10))

#1D ARRAY
arru = np.array([1,2,3,4,5])
print(arr)

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

print("NDIM:",arr.ndim)
print("First Index:",arr[1])

arr = np.array([[1,2,3],[4,5,6]])
print("1nd element on 1st row",arr[0,2])

l3 = np.array([[1,2,3],[4,5,6]])
print('2nd element in rows',l3[0])#[1,2,3]
print('Index Element from 2nd dim:',l3[1,-2])#5
print('4th after:',arr[:1])

print('arru',arru[-3:-1])
print('Increment',arru[::2])

