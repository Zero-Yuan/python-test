# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:06:53 2019

@author: yuan
"""

import turtle

turtle.screensize(400, 300, "black")

def draw_branch(branch_length):
    
    if branch_length > 5:
        turtle.color('brown')
        #right
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - 15)
        #left
        turtle.left(40)
        draw_branch(branch_length - 15)
        #back
        turtle.right(20)
        turtle.backward(branch_length)
    
def main():
       
    turtle.left(90)
    turtle.penup()
    turtle.backward(220)
    turtle.pendown()
    
    draw_branch(110)
    turtle.exitonclick()

if __name__ == '__main__':
    main()