import numpy as np 
import math  as mt 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import serial 
import time
#import keyboard as kb 
import continuous_threading
#import ctypes
import struct,re
import pandas as pd


ser = serial.Serial('COM3')
ser.baudrate = 115200
ser.timeout = 1
n = 25
SPD1,SPDT,corr,SPD3 = [],[],[],[]
Parser = pd.DataFrame()
ser_data = []
reading = True


 

def data_thread(delay):
    for i in range(10):
        #ser.flush()
        while(ser.inWaiting()==0):
                pass
        try:
            raw_data = ser.readline().decode("ascii")
            t_data=[float(val) for val in raw_data.split(';')]
            SPD1.append(t_data[0])
            SPDT.append(t_data[1])
            SPD3.append(t_data[2])
            
            ser.flush()
            time.sleep(delay)
        except: UnicodeDecodeError    
        
        
        

        

th = continuous_threading.ContinuousThread(target=data_thread,args=[1*10**-3])
th.start()
time.sleep(1)
th.stop()

Parser["SPD1"] = SPD1
Parser["SPDT"] = SPDT
Parser["SPD3"] = SPD3



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
      
    
    data = list(new_data)   
    if data[1]==50-data[0]:
        corr.append(data[0]/n)
        hl2.set_data(corr,np.ones(len(corr))*2-corr)
    else:    
        SPD1.append(data[0]/n)
        SPDT.append(data[1]/n)
        hl.set_data(SPD1,SPDT)
   
    #plt.pause(0.01)
    return lines

#ani = FuncAnimation(fig,
#                    update_line,
#                    fargs=ser_data,
#                    frames=10,
#                    interval=50)



#plt.show()







