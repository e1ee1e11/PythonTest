# -*- coding: utf8 -*-

def BMI(cm, kg):
        cm = round(float(cm/100), 2) #round(a, 2) 將a四捨五入到小數點第2位
        cm = round(float(cm*cm), 2)  #float(x) 將int x 變成 float x
        n = round(float(kg/cm), 2)
        return n

