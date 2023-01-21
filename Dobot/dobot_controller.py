import pydobot
from serial.tools import list_ports
from math import atan2, sqrt, acos, sin, degrees, cos, radians
from matrix import matrix

ports = [p.device for p in list_ports.comports()]

for i, port in enumerate(ports):
    print(f"{i}: {port}")

port = ports[int(input("Vælg en port: "))]

try:
    dobot = pydobot.Dobot(port=port)
except:
    print("Fejl, kunne ikke forbinde til robotten")
print("Forbindelse oprettet")

L2 = 150
L3 = 30
L4 = 150
L5 = 60
mode = pydobot.enums.PTPMode.MOVJ_ANGLE


def moveToCord(px, py, pz, vinkel):
    theta1 = atan2(py, px)
    L6 = sqrt(px*px+py*py)-L3-L5
    L7 = sqrt(pz*pz+L6*L6)
    phi1 = atan2(pz, L6)
    phi2 = acos((L7*L7+L2*L2-L4*L4)/(2*L7*L2))
    phi3 = acos((L4*L4+L2*L2-L7*L7)/(2*L2*L4))
    theta1 = degrees(theta1)
    theta2 = 90 - degrees(phi1) - degrees(phi2)
    theta4 = 90 + theta2 - degrees(phi3)
    theta6 = vinkel - theta1

    dobot._set_ptp_cmd(round(theta1, 5), round(theta2, 5), round(theta4, 5), round(theta6, 5), mode=mode, wait=True)


def movetomatrix(m):
    moveToCord(m.data[0][3], m.data[1][3], m.data[2][3], degrees(acos(m.data[0][0])))


def get_pose(t1, t2, t4, t6):
    t1 = radians(t1)
    t2 = radians(t2)
    t4 = radians(t4)
    t6 = radians(t6)
    data = [[-sin(t1)*sin(t6)+cos(t1)*cos(t6), -cos(t1)*sin(t6)-sin(t1)*cos(t6), 0, (90+L4*cos(t4)+L2*cos(t2-radians(90)))*cos(t1)],
            [cos(t1)*sin(t6)+sin(t1)*cos(t6), -sin(t1)*sin(t6)+cos(t1)*cos(t6), 0, sin(t1)*(90+L3*cos(t4)+L2*cos(t2-radians(90)))],
            [0, 0, 1, -L4*sin(t4)-L2*sin(t2-radians(90))],
            [0, 0, 0, 1]]
    data = [[round(data[x][y], 4) for y in range(4)] for x in range(4)]
    postioin = matrix(4, 4, data)
    return postioin


def get_dobot_pos():
    (_, _, _, _, j1, j2, j3, j4) = dobot.pose()
    return get_pose(j1, j2, j3, j4)


moveToCord(300, -100, 0, 50)
# input()
m = get_dobot_pos()
m.print()
transformation = matrix.tranformation(0, 0, 0, -100, 0, 0)
print("")
transformation.print()
print("")
reslut = m * transformation
print("")
reslut.print()

movetomatrix(reslut)
m = get_dobot_pos()
m.print()

# input()

step_count = 7
p1 = (170, 150, 110)
p2 = (290, -150, -30)
step = ((p2[0]-p1[0])/step_count, (p2[1]-p1[1]) / step_count, (p2[2]-p1[2])/step_count)
while(True):
    for i in list(range(step_count+1))+list(reversed(range(step_count+1))):
        moveToCord(p1[0]+step[0]*i, p1[1]+step[1]*i, p1[2]+step[2]*i, 90)
