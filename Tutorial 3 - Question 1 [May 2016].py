Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from matplotlib import pyplot as plt
>>> from numpy.fft import fft,ifft
>>> import numpy
>>> 
>>> #Question 1: Write a function that will shift an array by an arbitrary amount using a convolution. Plot a gaussian that started in the cebtre of the array shifted by half the array length. 
>>> 
>>> def makeshift(x,n=0):
	zerocvec=0*x
	zerovec[n]=1
	vecft=fft(zerovec)
	xft=fft(x)
	return numpy.real(ifft(xft*vecft))

>>> if __name__=='main__':
	x=numpy.arange(-30,30,0.1)
	sigma=2
	y=numy.exp(-0.5*x**2/sigma**2)
	yshift=makeshift(y,y.sie/2)
	plt.ion()
	plt.plot(x,y)
	plt.plot(x,yshift)
	plt.show()
	
