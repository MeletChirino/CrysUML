from crysuml.Sequence import Sequence
from crysuml.functions import *
from crysuml.UseCase import Actor
from cases import *
from actors import *

gui = Actor(
        name = 'GUI',
        type = "component"
        )
actor_list = get_list(Actor)
actor_list.append(gui)

single_move = Sequence(
        name = "Single Move",
        actors = get_list(Actor),
        links = [
            link(case=single_move),
            ],
        sequence_list = [
            message(starts=operator, ends=raspi, message="", categorie="politesse"),
            activate(actor=operator),
            activate(actor=raspi),
            reponse(starts=raspi, ends=operator, message="Hi there!", categorie="politesse"),
            message(starts=raspi, ends=raspi, message="Hate him :/", categorie="pensees"),
            message(starts=raspi, ends=operator, message="Are you ok?", categorie="politesse"),
            reponse(starts=operator, ends=raspi, message="Yes", categorie="politesse"),
            deactivate(actor=operator),
            message(starts=raspi, ends=raspi, message="Damn it", categorie="pensees"),
            deactivate(actor=raspi),
            ]
        )

test = Sequence(
        name = "Test",
        #actors = actor_list,
        actors = get_list(Actor),
        links = [
            link(case=single_move),
            ],
        sequence_list = [
            message(starts=operator, ends=gui, message="test connection"),
            activate(actor=operator),
            activate(actor=raspi),
            activate(actor=gui),
            loop(condition="for 3 times"),
            message(starts=gui, ends=raspi, message="test_connection()", categorie="communication_api"),
            alt(condition="good connection"),
            message(starts=raspi, ends=raspi, message="starting_test()", categorie="test_commands"),
            message(starts=raspi, ends=gui, message="send_status(operator)", categorie="communication_api"),
            reponse(starts=gui, ends=operator, message="status"),
            message(starts=gui, ends=gui, message="break(loop)"),
            elsif(condition="connection timeout"),
            message(starts=gui, ends=gui, message="try_again()"),
            deactivate(actor=operator),
            deactivate(actor=raspi),
            deactivate(actor=gui),
            end(),
            end()
            ]
        )

single_move.create()
test.create()
