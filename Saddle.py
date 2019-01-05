import math
# For get the coordinate value of points
"""
Use the first algorithm from the paper
"""
'''
It will support the second algorithm from the paper in future
'''


class Saddle:
    branch_radius = 109.3 / 2
    header_radius = 216.3 / 2
    theta_angle_step = 15

    def print_points(self):
        theta = 0
        while theta <= 360:
            theta_radian = math.radians(theta)
            x = self.branch_radius * math.cos(theta_radian)
            y = self.branch_radius * math.sin(theta_radian)
            z = math.sqrt(self.header_radius ** 2 - (self.branch_radius * math.sin(theta_radian)) ** 2)
            dihedral_radius = math.acos(self.branch_radius * (math.sin(theta_radian) ** 2) / self.header_radius)
            dihedral_angle = math.degrees(dihedral_radius)
            euler_y = (180 - dihedral_angle) / 2 - 180
            print("{0}: [[{1:.1f},{2:.1f},{3:.1f}],[{4:.0f},{5:.0f},{6:.0f}]]".format(theta, x, y, z, theta, euler_y, 0))
            if theta < 360 < (theta + self.theta_angle_step):
                theta = 360
            else:
                theta = theta + self.theta_angle_step


x = Saddle.Saddle()
x.print_points()
