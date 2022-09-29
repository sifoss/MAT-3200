import numpy as np, matplotlib.pyplot as plt

class Wave_Equation:
    def __init__(self):
        pass

    def make_grid(self, x0=0, xn=1, nx=100,\
                        t0=0, tn=1, nt=100):
        self.x = np.linspace(x0, xn, nx)
        self.t = np.linspace(t0, tn, nt)
        self.hx = (xn - x0)/nx
        self.ht = (tn - t0)/nt
        self.s = self.ht**2/self.hx**2
        self.nt, self.nx = nt, nx

    def solve(self, gamma, eta, phi, psi):
        gamma = gamma(self.t)
        eta = eta(self.t)
        phi = phi(self.x)
        psi = psi(self.x)
        nx, nt = self.nx, self.nt
        u = np.zeros((nx, nt)) 
        u[:, 0] = phi
        u[0, 0] = gamma[0] 
        u[-1,0] = eta[0]
        s, ht = self.s, self.ht
        
        # Setting second time step
        for i in range(1, nx-1):
            u[i, 1] = 0.5*s*(phi[i+1] + phi[i-1]) + (1-s)*phi[i] + ht*psi[i]
        u[0, 1] = gamma[1]
        u[-1, 1] = eta[1]
        
        #solve
        for i in range(1, nt-1):
            u[0, i] = gamma[i]
            u[-1, i] = eta[i]
            for j in range(1, nx-1):
                u[j, i+1] = s*(u[j+1, i] + u[j-1,i]) + 2*(1-s)*u[j,i] - u[j,i-1]

        return u
