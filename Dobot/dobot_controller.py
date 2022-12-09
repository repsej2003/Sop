import pydobot
from serial.tools import list_ports
from math import atan2, sqrt, acos, asin, sin, degrees

#ports = [p.device for p in list_ports.comports()]

# for i, port in enumerate(ports):
#    print(f"{i}: {port}")

#port = ports[int(input("Vælg en port: "))]

try:
    dobot = pydobot.Dobot(port="COM7")
except:
    print("Fejl, kunne ikke forbinde til robotten")
print("Forbindelse oprettet")

L1 = 150
L2 = 30
L3 = 150
L4 = 60
mode = pydobot.enums.PTPMode.MOVJ_ANGLE


def moveToCord(px, py, pz, vinkel):
    theta1 = atan2(py, px)
    x = sqrt(px*px+py*py)-L2-L4
    h = sqrt(pz*pz+x*x)
    phi1 = atan2(pz, x)
    phi2 = acos((h*h+L1*L1-L3*L3)/(2*h*L1))
    phi3 = acos((L3*L3+L1*L1-h*h)/(2*L1*L3))
    theta1 = degrees(theta1)
    theta2 = 90 - degrees(phi1) - degrees(phi2)
    theta4 = 90 + theta2 - degrees(phi3)
    theta6 = - vinkel - theta1
    #print(f'j1:{theta1} j2:{theta2} j3:{theta4} j4:{theta6}')
    dobot._set_ptp_cmd(round(theta1, 5), round(theta2, 5), round(theta4, 5),
                       round(theta6, 5), mode=mode, wait=True)
    (x, y, z, r, j1, j2, j3, j4) = dobot.pose()
    #print(f'x:{x} y:{y} z:{z} r:{r} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')
    print(
        f'Diff: x: {round(px-x,2)} y: {round(py-y,2)} z: {round(pz-z,2)} r: {round(vinkel-r,2)}')


step_count = 7
p1 = (170, 150, 110)
p2 = (290, -150, -30)
step = ((p2[0]-p1[0])/step_count, (p2[1]-p1[1]) /
        step_count, (p2[2]-p1[2])/step_count)
while(True):
    for i in list(range(step_count+1))+list(reversed(range(step_count+1))):
        moveToCord(p1[0]+step[0]*i, p1[1]+step[1]*i, p1[2]+step[2]*i, 90)
