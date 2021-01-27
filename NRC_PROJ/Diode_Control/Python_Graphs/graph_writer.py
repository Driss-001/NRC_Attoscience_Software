import numpy as np 
import math  as mt 
import matplotlib.pyplot as plt 
import serial 
import time

port_name = "COM3"
ser = serial.Serial()
ser.baudrate = 115200
ser.port = port_name
ser.reset_input_buffer()

