# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:35:18 2019
lambda函数
@author: yuan
"""

def main():
     
    USD_VS_RMB = 6.77
    currency_str_value = input('请输入带单位的货币金额：')  
    unit = currency_str_value[-3:] 
       #判断货币单位
    if unit == "CNY":
        exchange_rate = 1 / USD_VS_RMB
    elif unit == "USD":
        exchange_rate = USD_VS_RMB
    else:
        exchange_rate = -1
      #计算结果
    if exchange_rate != -1:
        in_money = eval( currency_str_value[:-3] )
        
        convert_currency = lambda x: x * exchange_rate
        
        out_money = convert_currency(in_money)
        print('兑换后的金额', out_money)
    else:
        print('-1')
#调用函数
if __name__ == '__main__':
    main()