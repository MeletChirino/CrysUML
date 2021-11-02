from crysuml.UseCase import Case
from crysuml.functions import link
from .actors import *

set_parameters = Case(
        name = 'Set Parameters (speed/acceleration)',
        links = [
            link(exigence='settings'),
            link(actor=motors, type='simple'),
            link(actor=operator, type='simple'),
            ]
        )
single_move = Case(
        name = "Manual mode",
        description = "In this mode we are going to drive the robot with manual buttons to place it where we want.",
        links = [
            link(actor=operator, type='simple'),
            link(actor=motors, type='simple'),
            link(exigence='manual_mode'),
            ]
        )
auto_move = Case(
        name = "Semi-Autonomous Mode",
        links = [
            link(exigence='functions'),
            link(actor=camera, type='simple'),
            link(actor=operator, type='simple'),
            ]
        )

receive_data = Case(
        name = 'Receive Data',
        description = 'From Lidar Groupe we are going to receive cartographie info. From Camera3d Group we are going to receive speed, position and status.',
        links = [
            link(actor=camera, type='simple'),
            link(actor=lidar, type='simple'),
            link(exigence='receive_info'),
            link(case=single_move, type='include'),
            link(case=auto_move , type='include'),
            ]
        )

