import xbox
import time
import ev3dev.ev3 as ev3

m_a = ev3.LargeMotor('outA')
m_b = ev3.LargeMotor('outB')


xbox = xbox.XBox()
xbox.start()

m_a.run_direct()
m_b.run_direct()

print('Running control')

while True:
    y1 = xbox.value['Y1']/32768.0
    y2 = xbox.value['Y2']/32768.0

    m_a.duty_cycle_sp = int(y1*100)
    m_b.duty_cycle_sp = int(y2*100)

 
