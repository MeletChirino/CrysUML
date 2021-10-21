from crysuml.UseCase import Actor

operator = Actor(
        name = 'Operator',
        description = 'Operator is going to say the robot what they should do'
        )
lidar = Actor(
        name='lidar',
        verbose_name = 'LiDar Groupe',
        description = 'This group is going to send us LiDar information',
        type = 'component',
        )
camera = Actor(
        name='camera',
        verbose_name = 'Camera 3D',
        description = 'This group is going to send us speed, position and acceleration because they have an accelerometer',
        type = 'component',
        )
motors = Actor(
        name='motors',
        verbose_name = 'Asservissement de moteurs',
        description = 'We are going to send to this group manual using info',
        type = 'component',
        )
"""
robot = Actor(
        name='robot',
        verbose_name='Robot',
        description = 'This is going to control the whole stuff',
        type='component'
        )"""
