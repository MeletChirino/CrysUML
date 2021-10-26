"""Components file"""
from crysuml.PhysicArch import *

pc_api = Component(
        name = "PC_API",
        description = "API pour etablir la communication entre le robot et l'interface graphique du PC",
        categorie = "communication",
        ports = (
            'socket_tcp',
            'lidar_data_send',
            'params',
            'robot_mecanics',
            'recv_position_data',
            'send_position_data',
            )
        )
robot_api = Component(
        name = 'robot_API',
        verbose_name = "Robot API",
        description = 'Partie de l\'API dedans le robot',
        categorie = 'communication',
        ports = (
            'socket_tcp',
            'bus_4355',
            'recv_position_data',
            'send_position_data',
            )
        )
robot = Component(
        name = 'robot',
        verbose_name = "Robot",
        description = 'Partie de l\'API dedans le robot',
        categorie = 'robot_functions',
        ports = (
            'bus_4355',
            )
        )
Qt_frame = Component(
        name = "Qt_frame",
        verbose_name = "Qt Frame",
        description = "Carre developpe avec Python et Qt pour montrer l'information",
        categorie = 'frontend',
        ports = (
            'lidar_widget',
            'params_widget',
            'mecanics_widget',
            )
        )
ros = Component(
        name = 'ROS',
        description = 'Program for processing and show lidar infor',
        categorie = 'data_process',
        ports = (
            'recv_lidar_data',
            'send_lidar_data',
            'recv_position_data',
            'send_position_data',
            )
        )
connections_list = [
        connect(# socket --> socket
            port(pc_api,'socket_tcp'),
            port(robot_api, 'socket_tcp'),
            bidirectional = True,
            ),
        connect(# bus inside robot
            port(robot_api,'bus_4355'),
            port(robot, 'bus_4355'),
            bidirectional = True,
            ),
        connect(
            port(ros, 'send_lidar_data'),
            port(Qt_frame, 'lidar_widget'),
            ),
        connect(# ros <-- qt frame
            port(Qt_frame, 'lidar_widget'),
            port(ros, 'recv_position_data'),
            ),
        connect(# api --> ros
            port(pc_api, 'lidar_data_send'),
            port(ros, 'recv_lidar_data'),
            ),
        connect(
            port(Qt_frame, 'params_widget'),
            port(pc_api, 'params'),
            ),
        connect(
            port(pc_api,'robot_mecanics'),
            port(Qt_frame, 'mecanics_widget'),
            ),
        connect(
            port(ros,'send_position_data'),
            port(pc_api, 'recv_position_data'),
            ),
        connect(
            port(pc_api, 'send_position_data'),
            port(robot_api, 'recv_position_data'),
            )

        ]
