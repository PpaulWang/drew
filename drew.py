import numpy as np
import matplotlib.pyplot as pl


data=np.loadtxt('/home/wcq/Desktop/out.out')
#
pl.plot(data[:,0],data[:,1],label='K = 2')
pl.plot(data[:,0],data[:,2],label='K = 4')
pl.plot(data[:,0],data[:,3],label='K = 6')
pl.plot(data[:,0],data[:,4],label='K = 8')
pl.plot(data[:,0],data[:,5],label='K = 10')
pl.plot(data[:,0],data[:,6],label='K = 12')
#
pl.title('The increasing of runtime for distinct L and K')
pl.xlabel('L')
pl.ylabel('runtime/(s)')

pl.axis([0,70,0,120],[1,1])
pl.legend()
pl.grid()
#pl.show()
pl.savefig('runtime_L_K.jpg')
