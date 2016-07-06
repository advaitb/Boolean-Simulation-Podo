import sys
import matplotlib.pyplot as plt
import boolean2
from boolean2 import Model , util


#Initial TimeSync Simulation on 07/01/2016

text = '''

ER = True
IGF1R = Random
IRS1 = Random
RAR = Random
MDM2 = Random
NEBL = Random
FOXA1 = Random
PITX2 = Random
ATF3 = Random
MDM2A = Random


2: RAR* = ER and not MDM2
2: IGF1R* = ER
2: IRS1* = IGF1R and not MDM2
# 9: MDM2A* = not MDM2
4: MDM2* = ((IRS1 and ER)or RAR) and not MDM2 
20: ATF3* = ((ER and PITX2) or RAR) and not MDM2 
20: FOXA1* = RAR or not ER
20: PITX2* = RAR and ER
20: NEBL* = (ATF3 and ER) or (FOXA1 and not ER and RAR) or (PITX2 and ER) 

''' 

model = Model( text = text , mode = 'time' )
model.initialize()
model.iterate(steps = 50)

plt.figure(1)
plt.subplot(121)
p2 = plt.plot( model.data["PITX2"] , 'oy-' )

p4 = plt.plot( model.data["NEBL"]  , '^g-' )
p5 = plt.plot( model.data["MDM2"]  , 'sm-' )

plt.legend([p2,p4,p5] , ['PITX2', 'NEBL' , 'MDM2'])

plt.subplot(122)
p1 = plt.plot( model.data["ATF3"] ,  'b-' )
p3 = plt.plot( model.data["FOXA1"] , 'r-' )

plt.legend([p1,p3] , ['ATF3' , 'FOXA1'])
plt.ylim((-0.5,1.5))
plt.show()
