import numpy as np 
import math  as mt 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import serial , struct,re ,time,sys
#import keyboard as kb 
import continuous_threading
import threading
#import ctypes
import pandas as pd


ser = serial.Serial('COM3')
ser.baudrate = 115200
ser.timeout = 1
SPD1,SPDT,corr1,SPD3, corr2,SPD3_corr1, SPD3_corr2 = [],[],[],[],[],[],[]
Parser = pd.DataFrame()
ser_data = []
 
fig = plt.figure()
 

progress_counter = 0
reading  = False
 
     


plt.ion

ax = fig.add_subplot()
ax.set_xlabel("SPD1")
ax.set_ylabel("SPDT")
hl1, = ax.plot(corr1,SPD3_corr1,'ro',c= "gray")
hl2, = ax.plot(corr2,SPD3_corr2,'ro',c= "red")

ax.set_aspect('auto')
ax.set_xlim(xmin=-1,xmax=3.1)
ax.set_ylim(ymin=-1,ymax=3.1)
   
lines = [hl1,hl2]


        


def update_line():

    
    for i in range(len(SPD1)):
   
        if SPD1[i]==SPDT[i]:
            corr1.append(SPD1[i])
            SPD3_corr1.append(SPD3[i])
    
    hl1.set_data(corr1,SPD3_corr1)
    
    for i in range(len(corr1)):
        if SPD3_corr1[i] ==3-corr1[i]:
            corr2.append(corr1[i])
            SPD3_corr2.append(SPD3_corr2[i])
    
    hl2.set_data(corr2,SPD3_corr2)

    #plt.pause(0.01)
    return lines

def Anim_Plot():

    ani = FuncAnimation(fig,
                    update_line,
                    fargs=None,
                    frames=10,
                    interval=100)

                   


def store_data():
    
    Parser["SPD1"] = SPD1
    Parser["SPDT"] = SPDT
    Parser["SPD3"] = SPD3

    file = "Experiment_Data.xlsx"
    writer = pd.ExcelWriter(file,engine = 'xlsxwriter') #save results in excel sheets
    Parser.to_excel(writer,sheet_name='Results') 
    writer.save()
    print("Data saved to file")
#plt.show()



def data_thread(run_num):
    #global progress_counter
    global  progress_counter
    global reading
    
    reading = True

    for i in range(run_num*10**3):
        #ser.flush()
        progress_counter += 1
        #reading = True
        try:
            raw_data = ser.readline().decode("ascii")
            t_data=[float(val) for val in raw_data.split(';')]
            SPD1.append(t_data[0])
            SPDT.append(t_data[1])
            SPD3.append(t_data[2])
        except: UnicodeDecodeError    

        

        #while(ser.inWaiting()==0):
        #       pass
        #reading = False
        ser.flush()
        time.sleep(10**-3)
    
    reading = False    
            



# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def main():
    run_time = 5 #int(sys.argv[1])*60
    th1 = threading.Thread(target=data_thread,args=(run_time,))
    #data_thread(run_time)
    th1.daemon = True
    #th2.daemon = True
 
    th1.start()
    th1.join()
    print(progress_counter)
    
    store_data()
    #printProgressBar(run_time,progress_counter)

    update_line()

    plt.show()
  

    

    

if __name__ == "__main__":
    
    main()

    #try:
    #    main()
    #except: 
    #    if sys.argv[1] == None:
    #        print("Please input the operation time in minutes(int)")
    



