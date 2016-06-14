Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # Question: Bonus Question
>>> 
>>> import math
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
	def __pow_simple__(self,val):
		ang=math.atan2(self.i,self.r)
		abs=math.sqrt(self.i*self.i+self.r*self.r)
		ans=self.copy()
		newabs=abs**val
		newang=ang*val
		ans.r=newabs*math.cos(newang)
		ans.i=newabs*math.sin(newang)
		return ans
	def __pow__(self,val):
		if isinstance(val,complexclass):
			ang=math.atan2(self.i,self.r)
		        myabs=math.sqrt(self.i*self.i+self.r*self.r)
		        myexp=complexclass(math.log(myabs),ang)
		        totexp=myexp*val
		        newabs=math.exp(totexp.r)
		        newang=complexclass(math.cos(totexp.i),math.sin(totexp.i))
		        return newang*newabs
		else:
			return self.__pow_simple__(val)
	def __repr__(self):
		if (self.i<0):
			return repr(self.r)+' - '+repr(-1*self.i) +'i
		
SyntaxError: EOL while scanning string literal
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
	def __pow_simple__(self,val):
		ang=math.atan2(self.i,self.r)
		abs=math.sqrt(self.i*self.i+self.r*self.r)
		ans=self.copy()
		newabs=abs**val
		newang=ang*val
		ans.r=newabs*math.cos(newang)
		ans.i=newabs*math.sin(newang)
		return ans
	def __pow__(self,val):
		if isinstance(val,complexclass):
			ang=math.atan2(self.i,self.r)
		        myabs=math.sqrt(self.i*self.i+self.r*self.r)
		        myexp=complexclass(math.log(myabs),ang)
		        totexp=myexp*val
		        newabs=math.exp(totexp.r)
		        newang=complexclass(math.cos(totexp.i),math.sin(totexp.i))
		        return newang*newabs
		else:
			return self.__pow_simple__(val)
	def __repr__(self):
		if (self.i<0):
			return repr(self.r)+' - '+repr(-1*self.i) +'i'
		else:
			return repr(self.r)+' + '+repr(-1*self.i) +'i'
	def __1shift__(Self,crud):
		self.i=-i*self.i
