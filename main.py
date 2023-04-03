#!/usr/bin/env pybricks-micropython

#Проприетарное программное обеспечение Коннора
#♥♥♥ Сделано с любовью ♥♥♥
#Тайрон версия 1.4


#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import math
import waypointfunction
import math
import objectavoidance
import barcodereader
import forklift
import time
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥

# Объявить Объект
ev3 = EV3Brick()
#gyro = GyroSensor(Port.S1)
ultrass = UltrasonicSensor(Port.S2)
leftMotor = Motor(Port.C)
rightMotor = Motor(Port.B)
forkliftMotor = Motor(Port.D)
colorRight = ColorSensor(Port.S1)
#colorLeft = ColorSensor(Port.S4)
tyrone = DriveBase(leftMotor,rightMotor,wheel_diameter = 68, axle_track = 173.2)
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
#Главный программ
barcodedb = [1010,1001,1100]

moveList = []
numPoints = int(input('Enter the number of points to move to: '))
for i in range(numPoints):
    xylist = []
    x = int(input('Enter X: '))
    y = int(input('Enter Y: '))
    xylist.append(x)
    xylist.append(y)
    moveList.append(xylist)

#Давай!
waypointfunction.waypoint(moveList,tyrone,ultrass,rightMotor,leftMotor)

#barcode = barcodereader.read(tyrone,colorRight,barcodedb)

#if (barcode in barcodedb):
#    print('BARCODE VERIFIED')
#    ev3.speaker.play_file('premade_Elli.wav')
#else:
#    print('BARCODE NOT FOUND')
#    ev3.speaker.play_file('premade_Bella.wav')

#forklift.init(forkliftMotor)
#tyrone.straight(120)
#forklift.pickup(forkliftMotor)
#tyrone.straight(120)
#forklift.drop(forkliftMotor)
#tyrone.straight(-120)
#forklift.reset(forkliftMotor)
