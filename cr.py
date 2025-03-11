import logging
import time
from threading import Thread

import cflib
from cflib.crazyflie import Crazyflie

logging.basicConfig(level=logging.ERROR)

link_uri = "radio://0/80/2M/E7E7E7E7E8"

cflib.crtp.init_drivers(enable_debug_driver=False)

crazyflie = Crazyflie()
crazyflie.connected.add_callback(link_uri)
crazyflie.open_link(link_uri)
print('Connecting to %s' % link_uri)

roll    = 0
pitch   = 0
yawrate = 0
thrust  = 37000 
crazyflie.commander.send_setpoint(0, 0, 0, 0)

for i in range(1,30):
# take off
    if i < 10:
        crazyflie.commander.send_setpoint(roll, pitch, yawrate, thrust)
        time.sleep(0.1)
# increase height
    elif i > 10 and i < 15:
        thrust = 38000
        crazyflie.commander.send_setpoint(0, 0, yawrate, thrust)
        time.sleep(0.1)
# for hovering
    else:
        roll    = 0
        pitch   = 0
        thrust = 36000 # just about enough to balance weight
        crazyflie.commander.send_setpoint(roll, pitch, yawrate, thrust)
        time.sleep(0.1)            
    print ('Sending data..', thrust)
    
Fland = thrust
while Fland > 20000: 
    Fland += -500
    crazyflie.commander.send_setpoint(roll, pitch, yawrate, Fland)
    time.sleep(0.1)
    print (Fland)
crazyflie.close_link()
