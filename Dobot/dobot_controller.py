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
150.00000000000003
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
    theta6 = vinkel + theta1
    print(f'j1:{theta1} j2:{theta2} j3:{theta4} j4:{theta6}')
    dobot._set_ptp_cmd(theta1, theta2, theta4, theta6, mode=mode, wait=True)
    (x, y, z, r, j1, j2, j3, j4) = dobot.pose()
    print(f'x:{x} y:{y} z:{z} r:{r} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')


#dobot._set_ptp_cmd(0, 0, 0, 0, mode=mode, wait=True)

moveToCord(300, 100, 50, 0)
