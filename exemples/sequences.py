from crysuml.Sequence import *
from crysuml.functions import *
from crysuml.UseCase import Actor
from .cases import *
from .actors import *

gui = Actor(
        name = 'GUI',
        type = "component"
        )
actor_list = get_list(Actor)
actor_list.append(gui)
set_parameters = Sequence(
        name = "Set Parameters",
        actors = get_list(Actor),
        links = [
            link(case=set_parameters),
            ],
        sequence_list = [
            activate(actor=operator),
            message(starts=operator, ends=gui, message="set_params(speed, acceleration)", categorie="frontend"),
            activate(actor=gui),
            message(starts=gui, ends=camera, message="speed_default(speed)", categorie="communication"),
            activate(actor=camera),
            message(starts=camera, ends=camera, message="save_speed(speed)", categorie="robot_functions"),
            reponse(starts=camera, ends=gui, message="save_status(OK)", categorie="communication"),
            message(starts=gui, ends=camera, message="accel_default(acceleration)", categorie="communication"),
            message(starts=camera, ends=camera, message="save_accel(accel)", categorie="robot_functions"),
            reponse(starts=camera, ends=gui, message="save_status(OK)", categorie="communication"),
            deactivate(actor=camera),
            reponse(starts=gui, ends=operator, message="Show('Parameters set')", categorie="frontend"),
            deactivate(actor=gui),
            deactivate(actor=operator),
            ],
        )
manual_mode_seq = Sequence(
        name = "Manual mode",
        actors = get_list(Actor),
        links = [
            link(case=single_move),
            ],
        sequence_list = [
            message(starts=operator, ends=gui, message="push(direction_button)", categorie="frontend"),
            activate(actor=operator),
            message(starts=gui, ends=motors, message="go_to(direction)", categorie="communication"),
            activate(actor=gui),
            message(starts=motors, ends=motors, message="go_to(direction)", categorie="communication"),
            activate(actor=motors),
            opt(condition="Error"),
            message(starts=motors, ends=gui, message='raise(code_error)', categorie="communication"),
            message(starts=gui, ends=operator, message='show(code_error)', categorie="frontend"),
            end(),
            ref(ref_sequence = receive_data, over=[operator, gui, camera]),
            end(),
            deactivate(actor=motors),
            deactivate(actor=gui),
            deactivate(actor=operator),
            ],
        )
receive_data = Sequence(
        name = 'Receive Data',
        actors = get_list(Actor),
        sequence_list = [
            activate(actor=gui),
            message(starts=gui, ends=lidar, message="get_lidar_info()", categorie="communication"),
            activate(actor=lidar),
            reponse(starts=lidar, ends=gui, message='lidar_info', categorie="data_process"),
            deactivate(actor=lidar),
            message(starts=gui, ends=gui, message='process_lidar_data()', categorie="data_process"),
            message(starts=gui, ends=operator, message='show(lidar_data)', categorie="frontend"),
            message(starts=gui, ends=camera, message="get_movement_info()", categorie="communication"),
            activate(actor=camera),
            reponse(starts=camera, ends=gui, message='movement_info', categorie="data_process"),
            deactivate(actor=camera),
            message(starts=gui, ends=operator, message='show(movement_data)', categorie="frontend"),
            deactivate(actor=gui),
            ],
        )
semi_auto_move = Sequence(
        name = "Semi-Autonomous Mode",
        actors = get_list(Actor),
        links = [
            link(seq = receive_data),
            ],
        sequence_list = [
            activate(actor=operator),
            message(starts=gui, ends=operator, message='show(lidar_data)', categorie="frontend"),
            message(starts=operator, ends=gui, message="select_point(x,y)", categorie="frontend"),
            message(starts=gui, ends=gui, message="process_points(x,y)", categorie="data_process"),
            activate(actor=gui),
            message(starts=gui, ends=camera, message="go_to(x,y)", categorie="communication"),
            activate(actor=camera),
            loop(condition="traject_status = in_progress"),
            message(starts=camera, ends=camera, message="read_sensors()", categorie="robot_functions"),
            message(starts=camera, ends=camera, message="traject_calcul()", categorie="robot_functions"),
            message(starts=camera, ends=camera, message="advance()", categorie="robot_functions"),
            ref(ref_sequence = receive_data, over=[operator, gui, lidar]),
            end(),
            end(),
            alt(condition="traject_status = Finished"),
            message(starts=camera, ends=gui, message='status(Finished)', categorie="communication"),
            message(starts=gui, ends=operator, message='show(Finished)', categorie="frontend"),
            elsif(condition="Error"),
            message(starts=camera, ends=gui, message='error(code_error)', categorie="communication"),
            message(starts=gui, ends=operator, message='show(code_error)', categorie="frontend"),
            end(),
            deactivate(actor=camera),
            deactivate(actor=operator),
            deactivate(actor=gui),
            ],
        )

semi_auto_move.create()
set_parameters.create()
receive_data.create()
manual_mode_seq.create()