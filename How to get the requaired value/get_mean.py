import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time



pullData = open("BTC-2GIVE.txt","r").read()
dataArray = pullData.split('\n')
xar = []
yar = []

for eachLine in dataArray:
   if len(eachLine)>1:
      
   	x,y= eachLine.split(',')
   	y=float(y)
   	print(len(dataArray))
   	print(len(eachLine))

