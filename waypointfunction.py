#!/usr/bin/env pybricks-micropython

#Проприетарное программное обеспечение Коннора
#♥♥♥ Сделано с любовью ♥♥♥
#Тайрон версия 1.3

import math
import time

#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
#функция чтобы перемещать Тайрона по точкам  Х и У 
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
def smartturn(tyrone, gyro, angle,rightMotor,leftMotor):
    """Precision turning due to the error created by simply using the functions
    provided to us in the pybricks library. This is specific to the Robot.
    """
    gyro.reset_angle(0)
    if angle < 0:
        while gyro.angle() > (angle-2):
            tyrone.drive(50,-50)
    
    elif angle > 0:
        while gyro.angle() < (angle-2):
            tyrone.drive(-50,50)
    else:
        return Null
    tyrone.stop()
    rightMotor.brake()
    leftMotor.brake()



def waypoint(coordlist,tyrone,ultrass,rightMotor,leftMotor):
    
    """Function takes a two dimensional list, called coordlist, of points to travel too, and a drivebase object, called tyrone to move
    the robot through multiple waypoints.
    """
    xcurrent = 0
    ycurrent = 0
    xsteps = 0
    ysteps = 0
    adjustedx = 0
    adjustedy = 0
    iterations = 0
    turncorrect = 0

    for i in range(len(coordlist)):
        adjustedx = coordlist[i][0] - xcurrent
        adjustedy = coordlist[i][1] - ycurrent
        xremainder = abs(adjustedx%200)
        xsteps = abs(math.floor(adjustedx/200))
        yremainder = abs(adjustedy%200)
        ysteps = abs(math.floor(adjustedy/200))
        if adjustedx != 0:
            if adjustedx > 0:
                tyrone.turn(90)
                tyrone.stop()
                rightMotor.brake()
                leftMotor.brake()
                turncorrect = -90
            else:
                tyrone.turn(-90)
                tyrone.stop()
                rightMotor.brake()
                leftMotor.brake()
                turncorrect = 90

        if adjustedy < 0:
            tyrone.turn(180)
            tyrone.stop()
            rightMotor.brake()
            leftMotor.brake()
            turncorrect = 180
        adjustedy = abs(adjustedy)
        adjustedx = abs(adjustedx)
        if adjustedx == 0:
                while iterations<ysteps:
                        while ultrass.distance() < 210: 
                            time.sleep(.2)
                        tyrone.straight(200)
                        iterations +=1
                if iterations == ysteps:
                    while ultrass.distance() < 210: 
                        time.sleep(.2)
                    tyrone.straight(yremainder)
                iterations = 0 

        if adjustedy == 0:
            while iterations<xsteps:
                    while ultrass.distance() < 210: 
                        time.sleep(.2)
                    tyrone.straight(200)
                    iterations +=1
            while ultrass.distance() < 210:
                time.sleep(.2)
            tyrone.straight(xremainder)
            iterations +=1
        tyrone.turn(turncorrect)
        tyrone.stop()
        rightMotor.brake()
        leftMotor.brake()
        iterations = 0
        xcurrent = coordlist[i][0]
        ycurrent = coordlist[i][1]
