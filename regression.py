import sys
import numpy as np
import matplotlib.pyplot as plt
import boolean2
from boolean2 import Model , util


#Initial Async Simulation on 07/01/2016

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
6: MDM2* = ((IRS1 and ER)or RAR) and not MDM2 
20: ATF3* = ((ER and PITX2) or RAR) and not MDM2 
20: FOXA1* = RAR or not ER
20: PITX2* = RAR and ER
20: NEBL* = (ATF3 and ER) or (FOXA1 and not ER and RAR) or (PITX2 and ER) 

''' 
text1 = '''

ER = Random
IGF1R = True
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
6: MDM2* = ((IRS1 and ER)or RAR) and not MDM2 
20: ATF3* = ((ER and PITX2) or RAR) and not MDM2 
20: FOXA1* = RAR or not ER
20: PITX2* = RAR and ER
20: NEBL* = (ATF3 and ER) or (FOXA1 and not ER and RAR) or (PITX2 and ER) 

''' 

text2 = '''

ER = Random
IGF1R = Random
IRS1 = Random
RAR = True
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
6: MDM2* = ((IRS1 and ER)or RAR) and not MDM2 
20: ATF3* = ((ER and PITX2) or RAR) and not MDM2 
20: FOXA1* = RAR or not ER
20: PITX2* = RAR and ER
20: NEBL* = (ATF3 and ER) or (FOXA1 and not ER and RAR) or (PITX2 and ER) 

''' 

coll = util.Collector() 
for i in xrange(150):

	model = Model( text=text , mode = 'async' )
	model.initialize()
	model.iterate( steps = 50 )

	nodes= model.nodes
	
	coll.collect( states = model.states , nodes = nodes )


	
avgs = coll.get_averages( normalize = True )

coll1 = util.Collector() 
for i in xrange(150):

	model1 = Model( text=text1 , mode = 'async' )
	model1.initialize()
	model1.iterate( steps = 50 )

	nodes1= model1.nodes
	
	coll1.collect( states = model1.states , nodes = nodes1 )


	
avgs1 = coll1.get_averages( normalize = True )

coll2 = util.Collector() 
for i in xrange(150):

	model2 = Model( text=text2 , mode = 'async' )
	model2.initialize()
	model2.iterate( steps = 50 )

	nodes2= model2.nodes
	
	coll2.collect( states = model2.states , nodes = nodes2 )


	
avgs2 = coll2.get_averages( normalize = True )

plt.title( " PITX2 regression vs NEBL" )

y = np.array(avgs["NEBL"])
x = np.array(avgs["PITX2"])
y1 = np.array(avgs1["NEBL"])
x1 = np.array(avgs1["PITX2"])
y2 = np.array(avgs2["NEBL"])
x2 = np.array(avgs2["PITX2"])

fit= np.polyfit(x,y, 1)
fit1 = np.polyfit(x1,y1,1)
fit2 = np.polyfit(x2,y2,1)
fit_fn = np.poly1d(fit)
fit_fn1 = np.poly1d(fit1)
fit_fn2 = np.poly1d(fit2)

s1 = plt.plot( x ,y, "yo" , fit_fn(x), '--y' )
s2 = plt.plot( x1 ,y1, "bo" , fit_fn1(x1), '--b' )
s3 = plt.plot( x2 ,y2, "mo" , fit_fn2(x2), '--m' )
plt.legend([s1,s2,s3] , ['ER', 'NEBL','IGF1R','NEBL', 'RAR', 'NEBL'])
plt.ylim((0,1))
plt.xlim((0,1))
plt.xlabel('Percent Probability of PITX2')
plt.ylabel('Percent Probability of NEBL')
plt.show()


#model.report_cycles()


#for node in model.data:
#	print node , model.data[node]
	
#model.report_cycles()
#print model.detect_cycles()

'''
#Plot Asynchronous run
plt.figure(1)
plt.subplot(121)
plt.title(" Async Run")
p1 = plt.plot( avgs["ATF3"] ,  'b-' )
p2 = plt.plot( avgs["PITX2"] , 'oy-' )
p3 = plt.plot( avgs["FOXA1"] , 'r-' )
p4 = plt.plot( avgs["NEBL"]  , '^g-' )
p5 = plt.plot( avgs["MDM2"]  , 'sm-' )

plt.legend([p1,p2,p3,p4,p5] , ['ATF3','PITX2', 'FOXA1' , 'NEBL' , 'MDM2'])
plt.ylim((0,1))

# Plot linear regression
plt.subplot(122)
plt.title("Transcriptional correlation with NEBL")
y = np.array(avgs["NEBL"])
x = np.array(avgs["ATF3"])
z = np.array(avgs["FOXA1"])
p = np.array(avgs["PITX2"])
fit= np.polyfit(x,y, 1)
fit1 = np.polyfit(z,y,1)
fit2 = np.polyfit(p,y,1)
fit_fn = np.poly1d(fit)
fit_fn1 = np.poly1d(fit1)
fit_fn2 = np.poly1d(fit2)
s1 = plt.plot( x ,y, "yo" , fit_fn(x), '--k' )
s2 = plt.plot( z ,y, "ro" , fit_fn1(z), '--k' )
s3 = plt.plot( p ,y, "bs" , fit_fn2(p), '--k' )
plt.legend([s1,s2,s3],['ATF3', 'FOXA1', 'PITX2'])
plt.ylim((0,1))
plt.xlim((0,1))
plt.show()
'''
 

