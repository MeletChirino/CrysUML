from crysuml.UseCase import Case
from crysuml.functions import link
from actors import *

single_move = Case(
        name = "Single move",
        links = [
            link(actor=operator, type='simple'),
            link(actor=raspi, type='simple'),
            link(exigence='messages'),
            ]
        )
test = Case(
        name = "Test",
        links = [
            link(actor=operator, type='simple'),
            link(actor=raspi, type='simple'),
            link(exigence='messages'),
            ]
        )
scan = Case(
        name = "Scan",
        links = [
            link(actor=operator, type='simple'),
            link(actor=raspi, type='simple'),
            link(exigence='messages'),
            ]
        )
receive_data = Case(
        name = 'Receive Data',
        links = [
            link(actor=raspi, type='simple'),
            link(exigence='wireless'),
            ]
        )
save_data= Case(
        name = 'Save data',
        links = [
            link(case=receive_data, type='include'),
            ]
        )
save_video = Case(
        name = 'Save Video',
        description = 'Users may want a video at the end of the scan',
        links = [
            link(case=save_data, type='extends'),
            link(exigence='final_report'),
            ]
        )
save_3d  = Case(
        name = 'Save 3D info',
        description = 'Users may want 3D info at the end of the scan',
        links = [
            link(case=save_data, type='extends'),
            link(exigence='final_report'),
            ]
        )
rt_data = Case(
        name = 'Show real-time data',
        links = [
            link(actor=operator, type='simple'),
            link(actor=raspi, type='simple'),
            link(exigence="real_time"),
            link(case=receive_data, type='extends'),
            ]
        )
final_data = Case(
        name = "Show final data",
        links = [
            link(actor=operator, type='simple'),
            link(exigence='final_report'),
            ]
        )
