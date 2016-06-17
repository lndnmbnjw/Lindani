Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> ##Question 2: ...write a class that contains masses and, x and y positions for a collection of particles....
>>> 
>>> import numpy
>>> class particles:
	def __init__(self,n=1000,G=1.0):
		self.x=numpy.random.randn(n)
		self.y=numpy.random.randn(n)
		self.m=numpy.ones(n)
		self.vx=numpy.zeros(n)
		self.vy=numpy.zeros(n)
		self.opts={}
		self.opts['n']=n
		self.opts['G']=G
	def calc_potential(self):
		pot=numpy.zeros(self.opts['n'])
		for i in range(0,self.opts['n']):
			dx=self.x[i]-self.x
			dy=self.y[i]-self.y
			r=numpy.sqrt(dx*dx+dy*dy)
			rinverse=1.0/r
			rinverse[i]=0
			potential[i]=self.m[i]+numpy.sum(self.opts['G']*self.m[i]*self.m*rinverse)
			return potential

		
>>> if __name__=='__main__':
	part=particles()
	pot=part.calc_potential()

