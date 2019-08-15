# -*- coding: utf-8 -*-
"""
Created on Sat May  4 12:28:30 2019
 #异常操作 处理
@author: yuan
"""

def main():
    
    y_or_n = input('是否退出程序(Y/N)？')
    
    while y_or_n != 'Y':
    
        print('请输入以下信息（用空格分割） ')        
        input_str = input('性别 体重（kg） 身高（cm） 年龄:')
        str_list = input_str.split(' ')
        
        try:
        
            gender = str_list[0]
            weight = float(str_list[1])
            height = float(str_list[2])
            age = int(str_list[3])
            
            if gender == '男':
                bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
            elif gender == '女':
                bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 665
            
            else:
                bmr = -1
           #输出结果
            if bmr != -1:
                print('您的性别：{}, 体重{}, 身高：{}  年龄：{}岁'.format(gender, height, weight, age))
                print('基础代谢率{}大卡'.format(bmr))
            else:
                print('暂不支持该数值')
            
           
        except ValueError:
            print('请输入正确的信息！')
        except IndexError:
            print('输入的信息过少！')
        except:
            print('程序异常！')
        
        print('####')
            
        y_or_n = input('是否退出程序(Y/N)？')

if __name__ == '__main__':
    main()