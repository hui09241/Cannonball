import sys
import math
import matplotlib.pyplot as plt 
#import numpy as np 
class Cannonball:
    def __init__(self,rad,rate):
        self.rad=rad
        self.rate=rate        
        self.px=0
        self.py=0
        self.vx=0
        self.vy=0
        self.t=0
        self.cos=math.cos(math.pi/180*rad)#cos=math.cos(angle)
        self.sin=math.sin(math.pi/180*rad)#sin=math.sin(angle)
        self.tan=math.tan(math.pi/180*rad)#tan=math.tan(angle)
    def tt(self):
        self.t=(self.sin*rate)/9.8 #angle=math.pi/180*rad#弧度轉角度->vy=math.sin(angle)*rate#速度y向量分量->t=vy/9.8#一半時間
    def getx(self,time):
        self.px=self.cos*rate*time #vx=math.cos(angle)*rate#速度x向量分量#px=vx*time
    def gety(self):
        self.py=self.tan*self.px-(9.8/(2*rate*rate*self.cos*self.cos))*self.px*self.px#py=tan*px-(9.8/(2*rate*rate*cos*cos))*px*px
        
rate=float(input("請輸入速度:"))
rad=float(input("請輸入角度:"))#輸入為弧度

ball=Cannonball(rad,rate)
#far=vx*t#一半長度
ball.tt()
#px=0
#py=0
time=0

while time<2*ball.t or time==2*ball.t :
        ball.getx(time)#px=vx*time
        ball.gety()#py=tan*px-(9.8/(2*rate*rate*cos*cos))*px*px
        plt.plot(ball.px,ball.py,"o")
        time=time+0.1

plt.show()

#print("速度",rate)
#print("角度x:",vx)
#print("角度y:",vy)