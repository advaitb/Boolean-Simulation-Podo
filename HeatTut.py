import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as c
'''
a =[1,2,3]
b=[4,5,6]
c=[7,8,9]

d =[ a,b,c]
print d


'''





a = [[0.1,0.6,0.457], [0.009,0.698,0.98], [0.8,0.6,0.7], [1, 0.5, 0.3]]
b = np.asarray(a)

plt.pcolor(b)
for y in range(b.shape[0]):
    for x in range(b.shape[1]):
        plt.text(x + 0.5, y + 0.5, '%.4f' % b[y, x],
                 horizontalalignment='center',
                 verticalalignment='center',
                 )
plt.colorbar()
plt.show()





'''

x = [1, 2, 3, 4, 5]  
y = [0.1, 0.2, 0.3, 0.4, 0.5]

intensity = [
    [5, 10, 15, 20, 25],
    [30, 35, 40, 45, 50],
    [55, 60, 65, 70, 75],
    [80, 85, 90, 95, 100],
    [105, 110, 115, 120, 125]
]


x, y = np.meshgrid(x, y)


intensity = np.array(intensity)


plt.pcolormesh(x, y, intensity)
plt.colorbar() 
plt.show()
'''