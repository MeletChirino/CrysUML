from crysuml.UseCase import Case
from crysuml.functions import link
from actors import *

commands = Case(
        name = 'Send commands',
        links = [
            link(actor=operator, type='simple'),
            link(exigence="messages"),
            ]
        )
single_command = Case(
        name = "Send single command",
        links = [
            link(case=commands, type='extends'),
            link(actor=raspi, type='simple'),
            ]
        )
many_command = Case(
        name = "Send group of commands",
        links = [
            link(case=commands, type='extends'),
            link(actor=raspi, type='simple'),
            ]
        )
receive_data = Case(
        name = 'Receive Data',
        links = [
            link(actor=raspi, type='simple'),
            ]
        )
rt_data = Case(
        name = 'Save data',
        links = [
            link(case=receive_data, type='extends'),
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
