#!/usr/bin/env pybricks-micropython

#Проприетарное программное обеспечение Коннора
#♥♥♥ Сделано с любовью ♥♥♥
#Тайрон версия 1.3

from pybricks.parameters import Port, Stop, Direction, Button, Color
import time
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
#функция чтобы перемещать Тайрона по точкам  Х и У 
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥

def read(tyrone,colorRight,barcodedb):
    barcode = []
    barcodedebug = []
    for i in range(4):
        time.sleep(.2)
        if colorRight.reflection()<=15:
            barcode.append('1')
        if colorRight.reflection()>=15:
            barcode.append('0')
        barcodedebug.append(colorRight.reflection())
        tyrone.straight(13)
    barcode.reverse()
    barcode = int(''.join(barcode))
    print(barcode)
    print(barcodedebug)
    return barcode