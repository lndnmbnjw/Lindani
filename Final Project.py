import numpy
from matplotlib import pyplot as plt
from numpy import *
from numpy.fft import fft, ifft, fftfreq
import time

class Particles:
    def __init__(self,n=1000,G=1.0,soft=0.1,L=1.0,m=1.0,dt=0.1):
        self.x=numpy.random.randn(n)
        self.y=numpy.random.randn(n)
        self.m=numpy.ones(n)*(1.0/n)
        self.vx=numpy.zeros(n)
        self.vy=numpy.zeros(n)
        self.opts={}
        self.opts['dt']=dt
        self.opts['n']=n
        self.opts['G']=G
        self.opts['soft']=soft
        self.k= numpy.zeros(n)

    def s_volume(self):              #q(charge) distribution on the grid.
        dx=self.x[i]-self.x[i+1:]
        return dx*dx*dx

    def rho_grid(self):
        rho=0.0
        qs=1
        mass=self.mass
        x=self.x
        y=self.y
        for i in range(len(x)):
            r_squared= (self.x[i]-self.x)**2+(self.y[i]-self.y)**2
            if (r_squared<qs):
                if (r_squared<0.5*qs):
                    rho += 8.0/numpy.pi*(1.0-6.0*r_squared**2 + 0.6*r_squared**3)
            else:
                rho += 16.0/numpy.pi* (1.0-r_squared)**3
        return rho*mass

    def rho_q(self):
        x=self.x
        y=self.y
        mass=self.mass 
        rho=0.0
        dx=self.x[i]-self.x[i+1:]
        for i in range(len(x)):
            if (abs(x[i]-x)) < dx and ( abs(y[i]-y) < dx ):
                rho += mass*(1.0 - abs(x[i]-x)/dx)* (1.0 - abs(y[i]-y)/dx)
                print("...")
        return rho


    def q_distrib(self):             #FFT on grid
        xx=self.x.shape[0]
        yy=self.y.shape[0]
        nx=numpy.arange(xx)
        ny=numpy.arange(yy)
        kx=nx.reshape((xx,1))
        Ky=ny.reshape((yy,1))
        k=kx*nx/xx + ky*ny/yy
        j=complex(0,1)
        K2=kx**2+ky**2
        q_rho=numpy.sum(numpy.exp(-2j*numpy.pi*k))
        q_rhofft=numpy.fft.fft(q_rho) 
        q_rho_f=(-4*numpy.pi/K2)*q_rhofft
        return q_rho

    def softened_pot(self):
        pot=0
        for i in range(0,self.opts['n']-1):
            dx=self.x[i]-self.x[i+1:]
            dy=self.y[i]-self.y[i+1:]
            rsqr=(dx*dx+dy*dy)
            rsqr[rsqr<self.opts['soft']]=self.opts['soft']
            r=numpy.sqrt(rsqr)
            r3inv=1.0/(r*rsqr)
            pot_1=(pot+numpy.sum(self.m[i]*self.m[i+1:]*1.0/r))*self.q_distrib() 
            pot=fft.ifft(pot_1) 
        return pot
        
    def get_forces(self):                                     #Force calculations
        self.fx=numpy.zeros(self.opts['n'])
        self.fy=numpy.zeros(self.opts['n'])
        for i in range(0,self.opts['n'-1]):
            self.fx[i]-=numpy.sum(dx*self.softened_pot()*self.m[i+1:])
            self.fy[i]-=numpy.sum(dx*self.softened_pot()*self.m[i+1:])
            self.fx[i+1:]+=dx*self.softened_pot()*self.m[i]
            self.fy[i+1:]+=dy*self.softened_pot()*self.m[i]
        return force

    def evolve(self):
        self.x+=self.vx*self.opts['dt']
        self.y+=self.vy*self.opts['dt']
        pot=self.softened_potential()
        self.vx+=self.fx*self.opts['dt']
        self.vy+=self.fy*self.opts['dt']
        kinetic=0.5*numpy.sum(self.m*(self.vx**2+self.vy**2))
        return pot+kinetic

if __name__=='__main__':
    particle=Particles()
    plt.ion()
    nstep=200
    kk=numpy.zeros(nstep)
    pp=numpy.zeros(nstep)
for xx in range(0,nstep):
    plt.clf()
    plt.plot(particle.x,particle.y,'*')
    plt.draw()