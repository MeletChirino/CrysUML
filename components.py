"""Components file"""
from crysuml.PhysicArch import *

communication_api = Component(
        name = "API",
        description = "API pour etablir la communication entre le robot et l'interface graphique du PC",
        categorie = "communication",
        ports = (
            'socket_tcp',
            'lidar_data_send',
            'params',
            )
        )
robot = Component(
        name = 'robot',
        verbose_name = "Robot",
        description = 'Partie de l\'API dedans le robot',
        categorie = 'robot_functions',
        ports = (
            'socket_tcp',
            )
        )
Qt_frame = Component(
        name = "Qt_frame",
        verbose_name = "Qt Frame",
        description = "Carre developpe avec Python et Qt pour montrer l'information",
        categorie = 'frontend',
        ports = (
            'lidar_widget',
            'movement_widget',
            'params_widget',
            )
        )
django = Component(
        name = "django",
        verbose_name = "djangoiFrame",
        description = "Carre developpe avec Python et Qt pour montrer l'information",
        categorie = 'frontend',
        ports = (
            'lidar_widget',
            'movement_widget',
            'params_widget',
            )
        )
ros = Component(
        name = 'ROS',
        description = 'Program for processing and show lidar infor',
        categorie = 'data_process',
        ports = (
            'recv_data',
            'send_data',
            )
        )
connections_list = [
        connect(# socket --> socket
            port(communication_api,'socket_tcp'),
            port(robot, 'sokcet_tcp'),
            ),
        connect(
            port(ros, 'send_data'),
            port(Qt_frame, 'lidar_widget'),
            ),
        connect(
            port(robot, 'socket_tcp'),
            port(ros, 'recv_data'),
            bidirectional = True,
            message = "Hi",
            )
        ]
