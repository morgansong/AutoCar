# -*- coding: utf-8 -*- 
import time
from RPI_Drive_Motor import Driver_Wheel_single

INT1 = []
INT2 = []

#wheel 1
w1_INT1 = 11
w1_INT2 = 12
INT1.append(w1_INT1)
INT2.append(w1_INT2)

#wheel 2
w2_INT1 = 15
w2_INT2 = 16
INT1.append(w2_INT1)
INT2.append(w2_INT2)

#wheel3
w3_INT1 = 35
w3_INT2 = 36
INT1.append(w3_INT1)
INT2.append(w3_INT2)

#wheel4
w4_INT1 = 37
w4_INT2 = 38
INT1.append(w4_INT1)
INT2.append(w4_INT2)



print(INT1,INT2)


for i in range(len(INT1)):
    print('start wheel {}'.format(str(i)))
    wheel = Driver_Wheel_single.Driver_Wheel_single(INT1[i], INT2[i])

    wheel.Forward()
    time.sleep(1)
    wheel.STOP()

    time.sleep(1)

    wheel.Backward()
    time.sleep(1)
    wheel.STOP()



