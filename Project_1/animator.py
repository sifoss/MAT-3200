import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
class Animator:
    def __init__(self, x, t, y1, y2, skip_frames=1):

        self.x = x
        self.t = t[::skip_frames]
        self.y1 = y1[:,::skip_frames]  #f(t, x)
        self.y2 = y2[:,::skip_frames]

    def animate(self, save=False):
        x, y1, y2 = self.x, self.y1, self.y2
        self.x_axis = [x[0], x[-1]]
        self.y_axis = [np.min(np.c_[y1, y2])-0.1, np.max(np.c_[y1, y2])+0.1]
        x_axis = self.x_axis
        y_axis = self.y_axis
        
        fig, ax = plt.subplots()
        ax.axis([x_axis[0],x_axis[1],y_axis[0],y_axis[1]])
        l1,l2 = ax.plot([],[], [], [])

        def an(i):
            l1.set_data(x, y1[:,i])
            l2.set_data(x, y2[:,i])

        self.ani = matplotlib.animation.FuncAnimation(fig, an, frames=len(self.t))
        
        
        if save==True:
            self.ani.save('coil.gif',writer='ffmpeg') 
            