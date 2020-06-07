# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:04:02 2020

@author: Rajitha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

rainc=pd.read_csv('WET_SEASON_RAINC.csv',sep=',')
rainnc=pd.read_csv('WET_SEASON_RAINNC.csv',sep=',')

#all_station data
A_rainc=rainc['Attapeu']
A_rainnc=rainnc['Attapeu']
B_rainc=rainc['Borkeo']
B_rainnc=rainnc['Borkeo']
C_rainc=rainc['Louangnumtha']
C_rainnc=rainnc['Louangnumtha']
D_rainc=rainc['Louangphabang']
D_rainnc=rainnc['Louangphabang']
E_rainc=rainc['Mkham']
E_rainnc=rainnc['Mkham']
F_rainc=rainc['Oudomxai']
F_rainnc=rainnc['Oudomxai']
G_rainc=rainc['Pakse']
G_rainnc=rainnc['Pakse']
H_rainc=rainc['Paksong']
H_rainnc=rainnc['Paksong']
I_rainc=rainc['Paksan']
I_rainnc=rainnc['Paksan']
J_rainc=rainc['Phonhong']
J_rainnc=rainnc['Phonhong']
K_rainc=rainc['Salavanh']
K_rainnc=rainnc['Salavanh']
L_rainc=rainc['Savannakhet']
L_rainnc=rainnc['Savannakhet']
M_rainc=rainc['Sayabouli']
M_rainnc=rainnc['Sayabouli']
N_rainc=rainc['Thakhek']
N_rainnc=rainnc['Thakhek']
O_rainc=rainc['Phongsaly']
O_rainnc=rainnc['Phongsaly']
P_rainc=rainc['Samnuea']
P_rainnc=rainnc['Samnuea']
Q_rainc=rainc['Vientiane']
Q_rainnc=rainnc['Vientiane']
R_rainc=rainc['Xiengkhouang']
R_rainnc=rainnc['Xiengkhouang']
S_rainc=rainc['Sekong']
S_rainnc=rainnc['Sekong']

#getting total rain for all stations
A_array=[]
B_array=[]
C_array=[]
D_array=[]
E_array=[]
F_array=[]
G_array=[]
H_array=[]
I_array=[]
J_array=[]
K_array=[]
L_array=[]
M_array=[]
N_array=[]
O_array=[]
P_array=[]
Q_array=[]
R_array=[]
S_array=[]

for x in range(len(A_rainc)):
    totrain=A_rainc[x]+A_rainnc[x]
    A_array.append(totrain)
    
for x in range(len(A_rainc)):
    totrain=B_rainc[x]+B_rainnc[x]
    B_array.append(totrain)

for x in range(len(A_rainc)):
    totrain=C_rainc[x]+C_rainnc[x]
    C_array.append(totrain)

for x in range(len(A_rainc)):
    totrain=D_rainc[x]+D_rainnc[x]
    D_array.append(totrain)

for x in range(len(A_rainc)):
    totrain=E_rainc[x]+E_rainnc[x]
    E_array.append(totrain)
    
for x in range(len(A_rainc)):
    totrain=F_rainc[x]+F_rainnc[x]
    F_array.append(totrain)
    
for x in range(len(A_rainc)):
    totrain=G_rainc[x]+G_rainnc[x]
    G_array.append(totrain)
    
for x in range(len(A_rainc)):
    totrain=H_rainc[x]+H_rainnc[x]
    H_array.append(totrain)
    
for x in range(len(A_rainc)):
    totrain=I_rainc[x]+I_rainnc[x]
    I_array.append(totrain)
    
for x in range(len(A_rainc)):
    totrain=J_rainc[x]+J_rainnc[x]
    J_array.append(totrain)
    
for x in range(len(A_rainc)):
    totrain=K_rainc[x]+K_rainnc[x]
    K_array.append(totrain)
    
for x in range(len(A_rainc)):
    totrain=L_rainc[x]+L_rainnc[x]
    L_array.append(totrain)
    
for x in range(len(A_rainc)):
    totrain=M_rainc[x]+M_rainnc[x]
    M_array.append(totrain)
    
for x in range(len(A_rainc)):
    totrain=N_rainc[x]+N_rainnc[x]
    N_array.append(totrain)
    
for x in range(len(A_rainc)):
    totrain=O_rainc[x]+O_rainnc[x]
    O_array.append(totrain)
    
for x in range(len(A_rainc)):
    totrain=P_rainc[x]+P_rainnc[x]
    P_array.append(totrain)

for x in range(len(A_rainc)):
    totrain=Q_rainc[x]+Q_rainnc[x]
    Q_array.append(totrain)
    
for x in range(len(A_rainc)):
    totrain=R_rainc[x]+R_rainnc[x]
    R_array.append(totrain)
    
for x in range(len(A_rainc)):
    totrain=S_rainc[x]+S_rainnc[x]
    S_array.append(totrain)

#print(Attapeu_array)
#getting different prameters
para=rainc['Para']
date=rainc['Date']

para_array=[]
date_array=[]
for i in para:
    para_array.append(i)
    
for x in date:  
    date_array.append(x[:10])

#calculate the relevant data for each parameter and their positions
para1 = [index for index in range(len(para_array)) if para_array[index] == 'para-1']
para2 = [index for index in range(len(para_array)) if para_array[index] == 'para-2']
para3 = [index for index in range(len(para_array)) if para_array[index] == 'para-3']
para4 = [index for index in range(len(para_array)) if para_array[index] == 'para-4']
para5 = [index for index in range(len(para_array)) if para_array[index] == 'para-5']
para6 = [index for index in range(len(para_array)) if para_array[index] == 'para-6']
para7 = [index for index in range(len(para_array)) if para_array[index] == 'para-7']
para8 = [index for index in range(len(para_array)) if para_array[index] == 'para-8']
para9 = [index for index in range(len(para_array)) if para_array[index] == 'para-9']
para10 = [index for index in range(len(para_array)) if para_array[index] == 'para-10']
para11 = [index for index in range(len(para_array)) if para_array[index] == 'para-11']
para12= [index for index in range(len(para_array)) if para_array[index] == 'para-12']

#getting data labels for wet 2-17 and wet 2018
days_2017=date_array[:int(len(para1)/2)]
days_2018=date_array[(int(len(para1)/2)):len(para1)]

#slicing the data for each parameter and create dictionary for each station
Attapeu={'para-1':A_array[para1[0]:para1[-1]], 'para-2':A_array[para2[0]:para2[-1]],'para-3':A_array[para3[0]:para3[-1]],'para-4':A_array[para4[0]:para4[-1]],'para-5':A_array[para5[0]:para5[-1]],'para-6':A_array[para6[0]:para6[-1]],'para-7':A_array[para7[0]:para7[-1]],'para-8':A_array[para8[0]:para8[-1]],'para-9':A_array[para9[0]:para9[-1]],'para-10':A_array[para10[0]:para10[-1]],'para-11':A_array[para11[0]:para11[-1]],'para-12':A_array[para12[0]:para12[-1]]}

Borkeo={'para-1':B_array[para1[0]:para1[-1]], 'para-2':B_array[para2[0]:para2[-1]],'para-3':B_array[para3[0]:para3[-1]],'para-4':B_array[para4[0]:para4[-1]],'para-5':B_array[para5[0]:para5[-1]],'para-6':B_array[para6[0]:para6[-1]],'para-7':B_array[para7[0]:para7[-1]],'para-8':B_array[para8[0]:para8[-1]],'para-9':B_array[para9[0]:para9[-1]],'para-10':B_array[para10[0]:para10[-1]],'para-11':B_array[para11[0]:para11[-1]],'para-12':B_array[para12[0]:para12[-1]]}

Louangnumtha={'para-1':C_array[para1[0]:para1[-1]], 'para-2':C_array[para2[0]:para2[-1]],'para-3':C_array[para3[0]:para3[-1]],'para-4':C_array[para4[0]:para4[-1]],'para-5':C_array[para5[0]:para5[-1]],'para-6':C_array[para6[0]:para6[-1]],'para-7':C_array[para7[0]:para7[-1]],'para-8':C_array[para8[0]:para8[-1]],'para-9':C_array[para9[0]:para9[-1]],'para-10':C_array[para10[0]:para10[-1]],'para-11':C_array[para11[0]:para11[-1]],'para-12':C_array[para12[0]:para12[-1]]}

Louangphabang={'para-1':D_array[para1[0]:para1[-1]], 'para-2':D_array[para2[0]:para2[-1]],'para-3':D_array[para3[0]:para3[-1]],'para-4':D_array[para4[0]:para4[-1]],'para-5':D_array[para5[0]:para5[-1]],'para-6':D_array[para6[0]:para6[-1]],'para-7':D_array[para7[0]:para7[-1]],'para-8':D_array[para8[0]:para8[-1]],'para-9':D_array[para9[0]:para9[-1]],'para-10':D_array[para10[0]:para10[-1]],'para-11':D_array[para11[0]:para11[-1]],'para-12':D_array[para12[0]:para12[-1]]}

Mkham={'para-1':E_array[para1[0]:para1[-1]], 'para-2':E_array[para2[0]:para2[-1]],'para-3':E_array[para3[0]:para3[-1]],'para-4':E_array[para4[0]:para4[-1]],'para-5':E_array[para5[0]:para5[-1]],'para-6':E_array[para6[0]:para6[-1]],'para-7':E_array[para7[0]:para7[-1]],'para-8':E_array[para8[0]:para8[-1]],'para-9':E_array[para9[0]:para9[-1]],'para-10':E_array[para10[0]:para10[-1]],'para-11':E_array[para11[0]:para11[-1]],'para-12':E_array[para12[0]:para12[-1]]}

Oudomxai={'para-1':F_array[para1[0]:para1[-1]], 'para-2':F_array[para2[0]:para2[-1]],'para-3':F_array[para3[0]:para3[-1]],'para-4':F_array[para4[0]:para4[-1]],'para-5':F_array[para5[0]:para5[-1]],'para-6':F_array[para6[0]:para6[-1]],'para-7':F_array[para7[0]:para7[-1]],'para-8':F_array[para8[0]:para8[-1]],'para-9':F_array[para9[0]:para9[-1]],'para-10':F_array[para10[0]:para10[-1]],'para-11':F_array[para11[0]:para11[-1]],'para-12':F_array[para12[0]:para12[-1]]}

Pakse={'para-1':G_array[para1[0]:para1[-1]], 'para-2':G_array[para2[0]:para2[-1]],'para-3':G_array[para3[0]:para3[-1]],'para-4':G_array[para4[0]:para4[-1]],'para-5':G_array[para5[0]:para5[-1]],'para-6':G_array[para6[0]:para6[-1]],'para-7':G_array[para7[0]:para7[-1]],'para-8':G_array[para8[0]:para8[-1]],'para-9':G_array[para9[0]:para9[-1]],'para-10':G_array[para10[0]:para10[-1]],'para-11':G_array[para11[0]:para11[-1]],'para-12':G_array[para12[0]:para12[-1]]}

Paksong={'para-1':H_array[para1[0]:para1[-1]], 'para-2':H_array[para2[0]:para2[-1]],'para-3':H_array[para3[0]:para3[-1]],'para-4':H_array[para4[0]:para4[-1]],'para-5':H_array[para5[0]:para5[-1]],'para-6':H_array[para6[0]:para6[-1]],'para-7':H_array[para7[0]:para7[-1]],'para-8':H_array[para8[0]:para8[-1]],'para-9':H_array[para9[0]:para9[-1]],'para-10':H_array[para10[0]:para10[-1]],'para-11':H_array[para11[0]:para11[-1]],'para-12':H_array[para12[0]:para12[-1]]}

Paksan={'para-1':I_array[para1[0]:para1[-1]], 'para-2':I_array[para2[0]:para2[-1]],'para-3':I_array[para3[0]:para3[-1]],'para-4':I_array[para4[0]:para4[-1]],'para-5':I_array[para5[0]:para5[-1]],'para-6':I_array[para6[0]:para6[-1]],'para-7':I_array[para7[0]:para7[-1]],'para-8':I_array[para8[0]:para8[-1]],'para-9':I_array[para9[0]:para9[-1]],'para-10':I_array[para10[0]:para10[-1]],'para-11':I_array[para11[0]:para11[-1]],'para-12':I_array[para12[0]:para12[-1]]}

Phonhong={'para-1':J_array[para1[0]:para1[-1]], 'para-2':J_array[para2[0]:para2[-1]],'para-3':J_array[para3[0]:para3[-1]],'para-4':J_array[para4[0]:para4[-1]],'para-5':J_array[para5[0]:para5[-1]],'para-6':J_array[para6[0]:para6[-1]],'para-7':J_array[para7[0]:para7[-1]],'para-8':J_array[para8[0]:para8[-1]],'para-9':J_array[para9[0]:para9[-1]],'para-10':J_array[para10[0]:para10[-1]],'para-11':J_array[para11[0]:para11[-1]],'para-12':J_array[para12[0]:para12[-1]]}

Salavanh={'para-1':K_array[para1[0]:para1[-1]], 'para-2':K_array[para2[0]:para2[-1]],'para-3':K_array[para3[0]:para3[-1]],'para-4':K_array[para4[0]:para4[-1]],'para-5':K_array[para5[0]:para5[-1]],'para-6':K_array[para6[0]:para6[-1]],'para-7':K_array[para7[0]:para7[-1]],'para-8':K_array[para8[0]:para8[-1]],'para-9':K_array[para9[0]:para9[-1]],'para-10':K_array[para10[0]:para10[-1]],'para-11':K_array[para11[0]:para11[-1]],'para-12':K_array[para12[0]:para12[-1]]}

Savannakhet={'para-1':L_array[para1[0]:para1[-1]], 'para-2':L_array[para2[0]:para2[-1]],'para-3':L_array[para3[0]:para3[-1]],'para-4':L_array[para4[0]:para4[-1]],'para-5':L_array[para5[0]:para5[-1]],'para-6':L_array[para6[0]:para6[-1]],'para-7':L_array[para7[0]:para7[-1]],'para-8':L_array[para8[0]:para8[-1]],'para-9':L_array[para9[0]:para9[-1]],'para-10':L_array[para10[0]:para10[-1]],'para-11':L_array[para11[0]:para11[-1]],'para-12':L_array[para12[0]:para12[-1]]}

Sayabouli={'para-1':M_array[para1[0]:para1[-1]], 'para-2':M_array[para2[0]:para2[-1]],'para-3':M_array[para3[0]:para3[-1]],'para-4':M_array[para4[0]:para4[-1]],'para-5':M_array[para5[0]:para5[-1]],'para-6':M_array[para6[0]:para6[-1]],'para-7':M_array[para7[0]:para7[-1]],'para-8':M_array[para8[0]:para8[-1]],'para-9':M_array[para9[0]:para9[-1]],'para-10':M_array[para10[0]:para10[-1]],'para-11':M_array[para11[0]:para11[-1]],'para-12':M_array[para12[0]:para12[-1]]}

Thakhek={'para-1':N_array[para1[0]:para1[-1]], 'para-2':N_array[para2[0]:para2[-1]],'para-3':N_array[para3[0]:para3[-1]],'para-4':N_array[para4[0]:para4[-1]],'para-5':N_array[para5[0]:para5[-1]],'para-6':N_array[para6[0]:para6[-1]],'para-7':N_array[para7[0]:para7[-1]],'para-8':N_array[para8[0]:para8[-1]],'para-9':N_array[para9[0]:para9[-1]],'para-10':N_array[para10[0]:para10[-1]],'para-11':N_array[para11[0]:para11[-1]],'para-12':N_array[para12[0]:para12[-1]]}

Phongsaly={'para-1':O_array[para1[0]:para1[-1]], 'para-2':O_array[para2[0]:para2[-1]],'para-3':A_array[para3[0]:para3[-1]],'para-4':O_array[para4[0]:para4[-1]],'para-5':O_array[para5[0]:para5[-1]],'para-6':O_array[para6[0]:para6[-1]],'para-7':O_array[para7[0]:para7[-1]],'para-8':O_array[para8[0]:para8[-1]],'para-9':O_array[para9[0]:para9[-1]],'para-10':O_array[para10[0]:para10[-1]],'para-11':O_array[para11[0]:para11[-1]],'para-12':O_array[para12[0]:para12[-1]]}

Samnuea={'para-1':P_array[para1[0]:para1[-1]], 'para-2':P_array[para2[0]:para2[-1]],'para-3':A_array[para3[0]:para3[-1]],'para-4':P_array[para4[0]:para4[-1]],'para-5':P_array[para5[0]:para5[-1]],'para-6':P_array[para6[0]:para6[-1]],'para-7':P_array[para7[0]:para7[-1]],'para-8':P_array[para8[0]:para8[-1]],'para-9':P_array[para9[0]:para9[-1]],'para-10':P_array[para10[0]:para10[-1]],'para-11':P_array[para11[0]:para11[-1]],'para-12':P_array[para12[0]:para12[-1]]}

Vientiane={'para-1':Q_array[para1[0]:para1[-1]], 'para-2':Q_array[para2[0]:para2[-1]],'para-3':A_array[para3[0]:para3[-1]],'para-4':Q_array[para4[0]:para4[-1]],'para-5':Q_array[para5[0]:para5[-1]],'para-6':Q_array[para6[0]:para6[-1]],'para-7':Q_array[para7[0]:para7[-1]],'para-8':Q_array[para8[0]:para8[-1]],'para-9':Q_array[para9[0]:para9[-1]],'para-10':Q_array[para10[0]:para10[-1]],'para-11':Q_array[para11[0]:para11[-1]],'para-12':Q_array[para12[0]:para12[-1]]}

Xiengkhouang={'para-1':R_array[para1[0]:para1[-1]], 'para-2':R_array[para2[0]:para2[-1]],'para-3':A_array[para3[0]:para3[-1]],'para-4':R_array[para4[0]:para4[-1]],'para-5':R_array[para5[0]:para5[-1]],'para-6':R_array[para6[0]:para6[-1]],'para-7':R_array[para7[0]:para7[-1]],'para-8':R_array[para8[0]:para8[-1]],'para-9':R_array[para9[0]:para9[-1]],'para-10':R_array[para10[0]:para10[-1]],'para-11':R_array[para11[0]:para11[-1]],'para-12':R_array[para12[0]:para12[-1]]}

Sekong={'para-1':S_array[para1[0]:para1[-1]], 'para-2':S_array[para2[0]:para2[-1]],'para-3':A_array[para3[0]:para3[-1]],'para-4':S_array[para4[0]:para4[-1]],'para-5':S_array[para5[0]:para5[-1]],'para-6':S_array[para6[0]:para6[-1]],'para-7':S_array[para7[0]:para7[-1]],'para-8':S_array[para8[0]:para8[-1]],'para-9':S_array[para9[0]:para9[-1]],'para-10':S_array[para10[0]:para10[-1]],'para-11':S_array[para11[0]:para11[-1]],'para-12':S_array[para12[0]:para12[-1]]}


