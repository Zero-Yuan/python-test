# -*- coding: utf-8 -*-
"""
Created on Mon May 13 22:36:31 2019

@author: yuan
"""
def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi

def  cal_pm_iaqi(pm_value):
    
    if 0 <= pm_value < 36:
        iaqi = cal_linear(0, 50, 0, 35, pm_value)
    elif 36 <= pm_value < 76:
        iaqi = cal_linear(50, 100, 35, 75, pm_value)
    elif 76 <= pm_value < 116:
        iaqi = cal_linear(100, 150, 75, 115, pm_value)
    elif 116 <= pm_value < 150:
        iaqi = cal_linear(150, 200, 115, 150, pm_value)
    elif 150 <= pm_value < 250:
        iaqi = cal_linear(200, 300, 150, 250, pm_value)
    elif 250 <= pm_value < 350:
        iaqi = cal_linear(300, 400, 250, 350, pm_value)
    elif 350 <= pm_value < 500:
        iaqi = cal_linear(400, 500, 350, 500, pm_value)
    else:
        pass
    
def cal_co_iaqi(co_val):
    if 0 <= co_val < 36:
        iaqi = cal_linear(0, 50, 0, 3, co_val)
    elif 36 <= co_val < 76:
        iaqi = cal_linear(50, 100, 2, 4, co_val)
    elif 76 <= co_val < 116:
        iaqi = cal_linear(100, 150, 4, 14, co_val)
    elif 116 <= co_val < 150:
        iaqi = cal_linear(150, 200, 14, 24, co_val)
    elif 150 <= co_val < 250:
        iaqi = cal_linear(200, 300, 24, 36, co_val)
    elif 250 <= co_val < 350:
        iaqi = cal_linear(300, 400, 36, 48, co_val)
    elif 350 <= co_val < 500:
        iaqi = cal_linear(400, 500, 48, 60, co_val)
    else:
        pass


def cal_aqi(param_list):
    
    pm_value = param_list[0]
    co_value = param_list[1]
    
    pm_iaqi = cal_pm_iaqi(pm_value)
    co_iaqi = cal_co_iaqi(co_value)
    
    aqi = max(iaqi_list)
    return aqi
    

def main():
    
    input_str = input('(1)请输入PM2.5: (2)CO: (用空格分割)')
    value = input_str.split(' ')
    
    pm_value = float(value[0])
    co_value = float(value[1])
    
    param_list = []
    param_list.append(pm_value)
    param_list.append(co_value)
    
    aqi_val = cal_aqi(param_list)
    
    print('空气质量指数：{}'.format(aqi_val))

if __name__ == '__main__':
    main()