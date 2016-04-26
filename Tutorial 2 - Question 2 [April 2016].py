Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> #April 2016, tutorial 2: Question 2
>>> #Integration of cos(x) from 0 to pi/2 for a range number of points using simple method (including 10,30,100,300,1000 points between 0 and pi/2).
>>> import numpy as np
>>> n0=0
>>> n1=np.pi/2
>>> increments=[(n1-n0)/10,(n1-n0)/30,(n1-n0)/100,(n1-n0)/300,(n1-n0)/1000]
>>> for dn in increments:
	n=np.arange(n0,n1,dn)
	m=np.cos(n)
	tot=m.sum()*dn
	print 'integral is ' + repr(tot) + ' with dn=' + repr(dn)

	
integral is 1.0764828026941022 with dn=0.15707963267948966
integral is 1.025951465275319 with dn=0.05235987755982988
integral is 1.0078334198735821 with dn=0.015707963267948967
integral is 1.0026157092462991 with dn=0.005235987755982988
integral is 1.0007851925466307 with dn=0.0015707963267948967
>>> 
#As the number of dn go up or increases, the value of the integral gets closer to the actual value of the integral.When the number of dn decreases, the value of the integral does not agree with the actual value.
