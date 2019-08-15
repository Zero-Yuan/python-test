# -*- coding: utf-8 -*-
"""
Created on Sun May 12 11:01:16 2019

matplotlib可视化 数据分析
plt.hist(data, bins)
date:列表
bins 边界

numpy 可算计算
@author: yuan
"""



import matplotlib.pyplot as plt
import numpy as np

#显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False



def main():  
    totaltime = int(input('请输入投掷次数：'))
    
    roll1_arr = np.random.randint(1,7, size=totaltime)
    roll2_arr = np.random.randint(1,7, size=totaltime)
    roll3_arr = np.random.randint(1,7, size=totaltime)
    result_arr = roll1_arr + roll2_arr +roll3_arr
    
    hist, bins = np.histogram(result_arr, bins=range(3,20))
    print(hist)
    print(bins)
         
    plt.hist(result_arr, bins=range(3,20), normed=1, edgecolor='grey', linewidth=1, rwidth=1)
    tick_labels = ['3点', '4点', '5点',
                   '6点', '7点', '8点', '9点', '10点', '11点', '12点','13点', '14点', '15点',
                   '16点', '17点', '18点']
    tick_pos = np.arange(3, 19) + 0.5
    plt.xticks(tick_pos, tick_labels)
    
    
    plt.title('骰子点数统计图片')
    plt.xlabel('点数')
    plt.ylabel('频率')
    
    
    plt.show()

if __name__ == '__main__':
    main()