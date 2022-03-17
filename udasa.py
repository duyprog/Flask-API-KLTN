import pandas as pd 
import numpy as np 
from nltk import flatten
class udasa:

    def read_value_from_csv(path):
        df_value = pd.read_csv(path)
        list_value = df_value.values.tolist()
        list_value = flatten(list_value)
        return list_value
    
    def initialize_window(N, i, n, X):
        wN = []
        for x in range(0, N):
            wN.append(X[i-N+x])
        return wN

    def cal_avg_med(wN):
        avg_med = 0
        med_X = np.median(wN)
        for i in range(len(wN)):
            avg_med += (1/len(wN))*np.median(abs(wN[i]-med_X))
        return avg_med
    
    def cal_D(avg_med, wN, n):
        med_Xi = np.median(abs(wN[-1] - np.median(wN)))
        D = med_Xi - ((n+1)/2)*avg_med
        return D 
    
    def cal_next_T(n, D, t_base):
        nD = n*D
        if -nD > np.log(np.finfo(type(nD)).max):
            return t_base*n 
        return (n + ((1-n)/(1+np.exp(-nD))))*t_base
      
pass


