Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> from numpy.fft import fft,ifft
>>> from matplotlib import pyplot as plt
>>> 
>>> def corr(n,m):
	assert(n.size==m.size)
	nft=fft(n)
	mft=fft(m)
	mftconj=numpy.conj(mft)
	return numpy.real(ifft(nft*mftconj))

>>> if __name__=='__main__':
	n=numpy.arange(-30,30,0.1)
	sigma=2
	m=numpy.exp(-0.5*n**2/sigma**2)
	mcorr=corr(m,m)
	plt.plot(n,mcorr)
	plt.show()

	
[<matplotlib.lines.Line2D object at 0x7f215b8d4710>]
