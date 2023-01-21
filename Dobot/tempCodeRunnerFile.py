
moveToCord(300, -100, 0, 50)
input()
m = get_dobot_pos()
m.print()
transformation = matrix.tranformation(0, 0, 0, -100, 40, 40)
print("")
transformation.print()
print("")
reslut = m * transformation
print("")
reslut.print()