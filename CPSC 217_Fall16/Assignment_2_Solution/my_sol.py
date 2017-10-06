from SimpleGraphics import *
import random


title = input("Enter the title of the chart: ")
cat = int(input("Enter the number of categories: "))
grd_size = int(input("Enter the grid size (between 10 and 400): "))
Y_label = input("Enter the labet for the Y-Axis: ")

# Setting the grid outline
setFill("White")
setOutline("black")
rect(100,100,600,400)

setFont("Times", "30", "bold")
text(400,50,title)

setFont("Times", "11", "bold")
text(50,300,Y_label)

y = 500
while(y >= 100):
    line(100,y,700,y)
    text(710,y,str(500-y),"w")
    y = y - grd_size

bar_width = int(600/cat) - 5

x = 100
for i in range(1,cat+1,1):
    print("Label category ",i,": ",end = '')
    lab_cat = input()
    print("Enter the value of category ",lab_cat,": ",end = '')
    bar_height = float(input())
    y = 500 - bar_height
    
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    setFill(r,g,b)
    rect(x,y,bar_width,bar_height)
    text(x+int(bar_width/2),515,lab_cat)
    x = x + bar_width + 5
    
    
    
    
