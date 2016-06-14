Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> #Question 2: ...write a class that contains masses and, x and y positions for a collection of particles....
>>> 
>>> import numpy as np
>>> class nbod:
	def __init__(self,n=10,G=6.673*10**-11):
		self.x1=np.random(n)
		self.x2=np.random(n)
		self.m1=np.ones(n)
	def potential(self):
		p=np.zeros(n)
		for i in range[0,n]:
			r=np.sqrt(dx*dx+dy*dy)
			p[i]=np.sum(G*self.m1[i]*self.m1[i+1]*r**-1)
		return p

	
>>> print 'the potential energy of every particle is' +p
