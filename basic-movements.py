from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()

print(me.get_battery())

#
me.takeoff()
me.send_rc_control(0,5 ,0,0)
sleep(2)
me.send_rc_control(20,0,0,0)
sleep(2)
me.send_rc_control(0,0,0,0)
me.flip_back()
sleep(2)
me.flip("right")
sleep(2)
me.send_rc_control(0,0,0,0)


me.land()
