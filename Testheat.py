import pylab as pl
import numpy as np




data = pl.random((3,3)) # 25x25 matrix of values

pl.pcolormesh(data)
for y in range(data.shape[0]):
    for x in range(data.shape[1]):
        pl.text(x + 0.5, y + 0.5, '%.4f' % data[y, x],
                 horizontalalignment='center',
                 verticalalignment='center',
                 )

pl.colorbar()
pl.show()