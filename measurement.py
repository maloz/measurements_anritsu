
"""
Name: Python automation measurments
Description: This is a test script to command an Anritsu to make automatic measurements
Requires: DAMS platform controller, Anritsu VNA 
PyVISA, NI VISA drivers and other SciPy modules
Author: Malo Zollikofer - étic S.A.
Date: 17.12.2018
"""
import os
import numpy as np
import pandas as pd
import visa, time

rm = visa.ResourceManager() 
print(rm.list_resources())

freq_list = [] #unit in HZ
#color_code = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

vna = rm.open_resource('TCPIP::192.168.1.201::INSTR') 
vna.open()
vna.timeout = 25000 #value in ms
vna.write(':FREQuency:SPAN 25000')
vna.write(':BANDwidth|BWIDth[:RESolution] 12500')
vna.write(':CHPower:BANDwidth|BWIDth:INTegration 12500')


vna.write(':CONFigure:COVerage') 
vna.write(':DISPlay:TRACe:FORMat:COVerage BER')

for i in range(len(freq_list)):
    vna.write(':FREQuency:CENTer '+ str(freq_list[i]))
    value = vna.query(':READ:COVerage?')
    print(str(freq_list[i]) + " " + value)

   



