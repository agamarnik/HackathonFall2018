import CoDrone
drone = CoDrone.CoDrone()
drone.pair(CoDrone.Nearest)
platformX = 0
while True:
    angles = drone.get_gyro_angles()
    if angles.ROLL != 0:
        platformX += angles.ROLL
        print(platformX)

