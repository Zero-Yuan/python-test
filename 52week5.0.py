# -*- coding: utf-8 -*-
"""
Created on Sat May  4 12:28:30 2019
 for
@author: yuan
"""
import math
import datetime

def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    
    money_list = []
    saved_money_list = []
    
    for i in range(total_week):
        
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        saved_money_list.append(saving)
        
        #print('第{}周，存入{}钱  累计金额{}'.format(i + 1, money_per_week, saving))
        money_per_week += increase_money
    return saved_money_list
    
def main():
    
    money_per_week = float(input('每周金额：'))
    increase_money = float(input('递增金额：'))
    total_week = int(input('周数：'))
    
    saved_money_list = save_money_in_n_weeks(money_per_week, increase_money, total_week)
    
    input_date_str = input('请输入日期（yyyy/mm/dd）：')
    input_date = datetime.datetime.strptime(input_date_str, '%Y/%m/%d')
    week_num = input_date.isocalendar()[1]
    print('第{}周的存款：{}元'.format(week_num , saved_money_list[week_num  - 1]))
    
    
        
if __name__ == '__main__':
    main()