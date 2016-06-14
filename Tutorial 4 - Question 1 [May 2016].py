Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>>#Question 1: Show from a few sample cases that your functions work.				
>>> class complexclass:
	def __init__(self,r=0,imag=0):
		self.r=r
		self.i=imag
	def copy(self):
		return complexclass(self.r,self.i)
	def __add__(self,val):
		ans=self.copy()
		if isinstance(val,complexclass):
			ans.r=ans.r+val.r
			ans.imag=ans.i+val.i
		else:
			ans.r=ans.r+val
		return ans
	def __mul__(self,val):
		ans=self.copy()
		if isinstance(val,complexclass):
			ans.r=self.r*val.r-self.i*val.i
			ans.i=self.r*val.i+self.i*val.r
		else:
			ans.r=ans.r*val
			ans.i=ans.i*val
		return ans
	def __sub__(self,val):
		ans=self.copy()
		if isinstance(val,complexclass):
			ans.r=ans.r+val.r
			ans.imag=ans.i-val.i
		else:
			ans.r=ans.r-val
		return ans
	def __div__(self,val):
		if isinstance(val,complexclass):
			val=val.copy()
			val.i=-1*val.i
			ans=self*val
			myabs=val.r**2+val.i**2
			ans=ans*(1.0/myabs)
		else:
			ans=self*(1.0/val)
		return ans
	def __repr__(self):
		if (self.i<0):
			return repr(self.r)+' - '+repr(-1*self.i) +'i'
		else:
			return repr(self.r)+' + '+repr(self.i) +'i'
	def __1shift__(self,crud):
		self.i=-1*self.i

		

