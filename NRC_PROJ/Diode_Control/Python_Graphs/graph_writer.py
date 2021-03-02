import numpy as np 
import math  as mt 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation,PillowWriter
import serial , struct,re ,time,sys ,queue ,continuous_threading ,threading ,serial.tools.list_ports
import pandas as pd


ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "Silicon Labs" in p.description:
        com  =p.name

ser = serial.Serial(com)
ser.baudrate = 600000
#ser.timeout = 10**-3
SPD1,SPDT,corr1,SPD3, corr2,SPD3_corr1, SPD3_corr2 = [],[],[],[],[],[],[]
Parser = pd.DataFrame()

trans_data_queue = queue.Queue()
 
fig = plt.figure()
 

progress_counter = 0
reading  = False
 
     


plt.ion

ax = fig.add_subplot()
ax.set_xlabel("SPD1")
ax.set_ylabel("SPDT")
hl1, = ax.plot(SPD1,SPDT,'ro',c= "gray")
hl2, = ax.plot(corr2,SPD3_corr2,'ro',c= "red")

#ax[1].set_ylabel("photon count")

ax.set_aspect('auto')
#ax.set_xlim(xmin=-1,xmax=3.1)
#ax.set_ylim(ymin=-1,ymax=3.1)
   
lines = [hl1,hl2]


        


def update_line(self):

    hl1.set_data(SPD1,SPDT)
    
    for i in range(len(corr1)):
        if SPD1 == SPDT:
            SPD3_corr1.append(SPD1[i])
    
    hl2.set_data(SPD3_corr1,SPD3_corr1)

    ax.set_xlim(xmin=-1,xmax=np.max(SPD1))
    ax.set_ylim(ymin=-1,ymax=np.max(SPDT))
    
    return lines
                


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



def data_thread():
    global progress_counter
    global  progress_counter
    global reading

    reading = True

    while reading:
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
        #ser.reset_input_buffer()
        #time.sleep(10**-3)

    
     
            
ani = FuncAnimation(fig,
                    update_line,
                    interval=50)

def handle_close(evt): #define plot window closing event
    
    global reading
    reading = False


fig.canvas.mpl_connect('close_event',handle_close)

start = time.time()

def main():


    #plot_refreshms = 10
    #sleep_time = 10**-3
    th1 = threading.Thread(target=data_thread)
    #data_thread(run_time)
    th1.daemon = True
 
    th1.start()
    
  
    plt.show()



    global end_time
    end_time = time.time()
    
    ani.save("Anim_Plot.gif", writer="pillow",fps=30)
    
    fig.savefig("Data_Plot.png")
    
    store_data()
    #printProgressBar(run_time,progress_counter)

    #update_line()
    
  

    


    

if __name__ == "__main__":
    
    main()
    global end_time
    t=end_time-start
    print("Elapsed Data Reading Time: "+str(round(t,2))+"s")
    
    
    print(len(SPD1),len(SPDT),len(SPD3))
    #try:
    #    main()
    #except: 
    #    if sys.argv[1] == None:
    #        print("Please input the operation time in minutes(int)")
    



