import numpy as np 
import math  as mt 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import serial 
import time
import keyboard as kb 

ser = serial.Serial('COM3')
ser.baudrate = 9600
ser.timeout = 1
n = 25
SPD1,SPDT,corr = [],[],[]

plt.ion

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel("SPD1")
ax.set_ylabel("SPDT")
hl, = ax.plot(SPD1,SPDT,'ro',c= "gray")
hl2, = ax.plot(SPD1,SPDT,'ro',c= "red")

lines = [hl,hl2]

ax.set_aspect('auto')
ax.set_xlim(xmin=-1,xmax=2.5)
ax.set_ylim(ymin=-1,ymax=2.5)

def update_line(new_data):
   
    ser.reset_input_buffer()
    raw_data = ser.read(2)
    data = list(raw_data)
    if data[1]==50-data[0]:
        corr.append(data[0]/n)
        hl2.set_data(corr,np.ones(len(corr))*2-corr)
    else:    
        SPD1.append(data[0]/n)
        SPDT.append(data[1]/n)
        hl.set_data(SPD1,SPDT)
   
    #plt.pause(0.01)
    return lines

ani = FuncAnimation(fig,
                    update_line,
                    frames=10,
                    interval=50)



plt.show()







