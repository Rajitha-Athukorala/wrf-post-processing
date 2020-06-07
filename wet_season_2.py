# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 20:07:39 2020

@author: Rajitha
"""
import pandas as pd
import os 

all_csv=[]
wet_season_rainc=[]

for root, dirs, files in os.walk('.'):
    for file in files:
        p=os.path.join(root,file)
        #print(p)
        all_csv.append((os.path.abspath(p)))
#print(all_csv)
for y in all_csv:
    temp=y
    if (temp.find('set4') != -1) :
        wet_season_rainc.append(temp)
    else:
        pass


rainc_A=[]
rainc_B=[]
rainc_C=[]
rainc_D=[]
rainc_E=[]
rainc_F=[]
rainc_G=[]
rainc_H=[]
rainc_I=[]
rainc_J=[]
rainc_K=[]
rainc_L=[]
rainc_M=[]
rainc_N=[]
rainc_O=[]
rainc_P=[]
rainc_Q=[]
rainc_R=[]
rainc_S=[]

#
#
#ind_rainc_A=[]
#ind_rainc_B=[]
all_ind_date=[]
ind_date=[]
all_ind_A=[]
all_ind_B=[]
all_ind_C=[]
all_ind_D=[]
all_ind_E=[]
all_ind_F=[]
all_ind_G=[]
all_ind_H=[]
all_ind_I=[]
all_ind_J=[]
all_ind_K=[]
all_ind_L=[]
all_ind_M=[]
all_ind_N=[]
all_ind_O=[]
all_ind_P=[]
all_ind_Q=[]
all_ind_R=[]
all_ind_S=[]

        
parameter=[]


for r in wet_season_rainc:
    data=pd.read_csv('{}'.format(r), sep=',')
    para=r[62:69]
    para=para.replace('\\','')
    rainc_A=data['Attapeu']
    rainc_B=data['Borkeo']
    rainc_C=data['Louangnumtha']
    rainc_D=data['Louangphabang']
    rainc_E=data['Mkham']
    rainc_F=data['Oudomxai']
    rainc_G=data['Pakse']
    rainc_H=data['Paksong']
    rainc_I=data['Paksan']
    rainc_J=data['Phonhong']
    rainc_K=data['Salavanh']
    rainc_L=data['Savannakhet']
    rainc_M=data['Sayabouli']
    rainc_N=data['Thakhek']
    rainc_O=data['Sekong']
    rainc_P=data['Phongsaly']
    rainc_Q=data['Samnuea']
    rainc_R=data['Vientiane']
    rainc_S=data['Xiengkhouang']

    
    timestamp=data['Date']
    for h in range(len(rainc_A)):
        ind_rainc_A=rainc_A[h]
        ind_rainc_B=rainc_B[h]
        ind_rainc_C=rainc_C[h]
        ind_rainc_D=rainc_D[h]
        ind_rainc_E=rainc_E[h]
        ind_rainc_F=rainc_F[h]
        ind_rainc_G=rainc_G[h]
        ind_rainc_H=rainc_H[h]
        ind_rainc_I=rainc_I[h]
        ind_rainc_J=rainc_J[h]
        ind_rainc_K=rainc_K[h]
        ind_rainc_L=rainc_L[h]
        ind_rainc_M=rainc_M[h]
        ind_rainc_N=rainc_N[h]
        ind_rainc_O=rainc_O[h]
        ind_rainc_P=rainc_P[h]
        ind_rainc_Q=rainc_Q[h]
        ind_rainc_R=rainc_R[h]
        ind_rainc_S=rainc_S[h]
        ind_date=timestamp[h]
        all_ind_date.append(ind_date)
        all_ind_A.append(ind_rainc_A)
        all_ind_B.append(ind_rainc_B)
        all_ind_C.append(ind_rainc_C)
        all_ind_D.append(ind_rainc_D)
        all_ind_E.append(ind_rainc_E)
        all_ind_F.append(ind_rainc_F)
        all_ind_G.append(ind_rainc_G)
        all_ind_H.append(ind_rainc_H)
        all_ind_I.append(ind_rainc_I)
        all_ind_J.append(ind_rainc_J)
        all_ind_K.append(ind_rainc_K)
        all_ind_L.append(ind_rainc_L)
        all_ind_M.append(ind_rainc_M)
        all_ind_N.append(ind_rainc_N)
        all_ind_O.append(ind_rainc_O)
        all_ind_P.append(ind_rainc_P)
        all_ind_Q.append(ind_rainc_Q)
        all_ind_R.append(ind_rainc_R)
        all_ind_S.append(ind_rainc_S)
        parameter.append(para)
        
print(parameter)
#for r in wet_season_rainc:
#    data_Borkeo=pd.read_csv('{}'.format(r), sep=',')
#    rainc=data_Borkeo['Borkeo']
#    timestamp=data_Borkeo['Date']
#    for h in range(len(rainc)):
#        Borkeo_ind_rainc=rainc[h]
#        Borkeo_ind_date=timestamp[h]
#        Borkeo_all_ind_date.append(ind_date)
#        Borkeo_all_ind_rainc.append(ind_rainc)

#print(all_ind_date)    
print(all_ind_A)
df=pd.DataFrame(list(zip(*[parameter,all_ind_date,all_ind_A,all_ind_B,all_ind_C,all_ind_D,all_ind_E,all_ind_F,all_ind_G,all_ind_H,all_ind_I,all_ind_J,all_ind_K,all_ind_L,all_ind_M,all_ind_N,all_ind_O,all_ind_P,all_ind_Q,all_ind_R,all_ind_S])),columns=['Para','Date','Attapeu','Borkeo','Louangnumtha','Louangphabang','Mkham','Oudomxai','Pakse','Paksong','Paksan','Phonhong','Salavanh','Savannakhet','Sayabouli','Thakhek','Sekong','Phongsaly','Samnuea','Vientiane','Xiengkhouang'])
df.to_csv('WET_SEASON_RAINNC.csv')
