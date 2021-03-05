import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

txt_files = ["Harmonic_spectrum_2ms","Harmonic_spectrum_500ms","Harmonic_spectrum_2ms_2","Harmonic_spectrum_500ms_2"]
xls_files = ["Experiment_Data_1_wSiliccrystal","Experiment_Data_2","Experiment_Data_3nolaser","Experiment_Data4_wSI"]


def xy_store_txt(txt_names):
    for i in range(len(txt_names)):
        with open(txt_names[i]+".txt","r") as file1:
            l = file1.readlines()
        
        x,y = [],[]
        
        for d in l[0].split():
            x.append(float(d))
        for d in l[1].split():
            y.append(float(d))    

        x_arr = np.array(x)
        y_arr = np.array(y)

  

        plt.plot(x_arr,y_arr,c="r")
        plt.xlabel("Spectral Unit SU (nm)")
        plt.ylabel("Arbitrary Counts AU")
        x_tick = np.linspace(np.max(x_arr),np.min(x_arr),10)
        y_tick = np.linspace(np.max(y_arr),np.min(y_arr),10)
        plt.xticks(x_tick)
        plt.yticks(y_tick)
        plt.savefig(txt_names[i]+".png")
        plt.cla()
        
    plt.close()

def xy_store_xls(xls_names):
    for i in range(len(xls_names)):
        xl = pd.ExcelFile(xls_names[i]+".xlsx")
        df =xl.parse(0)
        Time = df.iloc[:,3]
        SPD1 = df.iloc[:,1][Time<=10]
        SPD2 = df.iloc[:,2][Time<=10] 
        
        

        #print(SPD1[0:5])
        
       
        y_arr = np.array(SPD1,SPD2)
        x_arr = np.array(Time)
        bin = np.linspace(0.5,3.5,50)
        y_tick = np.linspace(0,3.5,20)

         
        
        plt.xlabel("Voltage Measured(V)")
        plt.ylabel("Arbitrary Counts (AU)")

        plt.hist(SPD1,bins = bin,color="b")
        plt.hist(SPD2,bins = bin,color="r")
        plt.legend(["SPD1","SPD2"])
        #plt.xticks(x_tick)
        #plt.yticks(y_tick)


        plt.savefig(xls_names[i]+".png")
        plt.cla()

    plt.close()    
           

#xy_store_txt(txt_files)
xy_store_xls(xls_files)        

