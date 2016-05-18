Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> #Question 3: Write a routine to take the correlation function of a Guassian (shifted by an arbitrary amount) with itself.
>>> 
>>> from matplotlib import pyplot as plt
>>> import numpy
>>> from numpy.fft import fft,ifft
>>> 
>>> def myshift(q,n=0):
	zerovec=0*q
	zerovec[n]=1
	vectft=fft(zerovec)
	qft=fft(q)
	return numpy.real(ifft(qft*vectft))

>>> def corr(q,r):
	assert(q.size==r.size)
	qft=fft(q)
	rft=fft(r)
	rftconj=numpy.conj(rft)
	return numpy.real(ifft(qft*rftconj))

>>> if __name__=='__main__':
	q=numpy.arange(-20,20,0.1)
	sigma=2
	r=numpy.exp(-0.5*q**2/sigma**2)
	rcorr=corr(r,r)
	rshift=myshift(r,r.size/4)
	meanerr=numpy.mean(numpy.abs(rcorr-rshiftcorr))
	print 'mean difference between the two correlation functions is ' + repr(meanerr)
	plt.plot(q,rcorr)
	plt.plot(q,rshiftcorr)
	plt.show()
