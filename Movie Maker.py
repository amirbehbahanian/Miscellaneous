# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:10:47 2019

@author: A02197412
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import animation
import mpl_toolkits.mplot3d.axes3d as p3

def section(i):
    df1=[]
    f=open('A:/Argon/Analysis/Main/Single Wave Interaction/k-Energy-Vg_Check/50K/2.00e+11/dump.PE.allsections.%s' %(i*200))
    x=f.read()
    x = x.split('\n')
    x = x[9:-1]
    x = [x[a].split() for a in range(len(x))]
    x = [[float(x[a][b]) for b in range(len(x[a]))] for a in range(len(x))]
    df1=pd.DataFrame(x)
    del(x)
    df1=df1.drop(columns=0)
    df1.columns=['c_PE', 'x', 'y', 'z', 'vx', 'vy', 'vz']
    df1=df1.reset_index(drop=True)
    df1=df1.drop([len(df1)-1])
    df1=df1.sort_values(by=['y'])
    return df1


def animate(i):
    
    y = section(i)['y']
    PE = section(i)['c_PE'] 
    z = section(i).loc[(section(i)['x']>2) & (section(i)['x']<3.5)]['z']
    yz = section(i).loc[(section(i)['x']>2) & (section(i)['x']<3.5)]['y']

    u=section(i)['vx']
    v=section(i)['vy']
    w=section(i)['vz']

    line[0].set_data(y, PE)
    line[1].set_data(yz, z)
    line[2].set_data(y, u)
    line[3].set_data(y, v)
    line[4].set_data(y, w)

    return line

fig=plt.figure(figsize=(18,10))
plt.subplots_adjust(hspace = 0.5, wspace = 0.3)
ax1 = fig.add_subplot(4, 4, (1,4))
ax2 = fig.add_subplot(4, 4, (5,8))
ax3 = fig.add_subplot(4, 4, (9,12))
ax4 = fig.add_subplot(4, 4, (13,14))
ax5 = fig.add_subplot(4, 4, (15,16))

line1, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], '.', markersize=4)
line3, = ax3.plot([], [], '.', markersize=1)
line4, = ax4.plot([], [], markersize=2)
line5, = ax5.plot([], [], markersize=2)
line = [line1, line2, line3, line4, line5]

ax1.set_xlim(0, 320)
ax1.set_ylim(-0.084725, -0.084750)
ax1.set_ylabel('Potential in $ev$')
ax1.grid(True,which='major')

ax2.set_xlim(0, 320)
ax2.set_ylim(5.30,5.6)
ax2.set_ylabel('Z pozition')
ax2.grid(True,which='major')

ax3.set_xlim(0, 320)
ax3.set_ylim(-0.002, 0.002)
#ax3.set_ylim(-0.1, 0.1)
ax3.set_title('$Position$')
ax3.set_ylabel('Vx')
ax3.set_xlabel('Y position in the section')
ax3.grid(True,which='major')

ax4.set_xlim(0, 320)
ax4.set_title('$V_y$')
ax4.set_ylim(-0.05, 0.05)
#ax4.set_xticks(np.arange(0,5394.4614200000005,1078.892284))
ax4.set_xlabel('Y position in the section')
ax4.set_ylabel('Velocity' r'$ (\frac{Angstrom}{Femtosecond})$')
ax4.grid(True,which='major')

ax5.set_xlim(0, 320)
#ax5.set_xticks(np.arange(0,5394.4614200000005,1078.892284))
ax5.set_ylim(-0.4, 0.4)
ax5.set_title('$V_z$')
ax5.set_xlabel('Y position in the section')
ax5.grid(True,which='major')

anim = animation.FuncAnimation(fig, animate, frames=2500, interval=20, blit=True)
#anim.save('35e5steps_threewaves_120sig_0.1eta_2%amp_shifted.mp4', writer='ffmpeg',fps=20)
