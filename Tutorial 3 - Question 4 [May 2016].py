Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> #Question 4: Write a routine to take the convolution of two arrays *without* any danger of wrapping around.
>>> 
>>> from matplotlib import pyplot as plt
>>> import numpy
>>> from numpy.fft import fft,ifft
>>> 
>>> def conv_nowrap(m,n):
	assert(m.size==n.size)
	mm=numpy.zeros(2*m.size)
	mm[0:m.size]=m
	nn=numpy.zeros(2*n.size)
	nn[0:n.size]=n
	mmft=fft(mm)
	nnft=fft(nn)
	vec=numpy.real(ifft(mmft*nnft))
	return vec[0:m.size]

>>> if __name__=='__main__':
	m=numpy.arange(-30,30,0.1)
	sigma=2
	n=numpy.exp(-0.5*m**2/sigma**2)
	n=n/n.sum()
	nconv=conv_nowrap(n,n)
	plt.plot(m,n)
	plt.plot(m,nconv)
	plt.show()

	
[<matplotlib.lines.Line2D object at 0x7f5cb08526d0>]
[<matplotlib.lines.Line2D object at 0x7f5cb0852950>]
