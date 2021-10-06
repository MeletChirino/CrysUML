from crysuml.Sequence import Sequence
from crysuml.functions import *
from cases import *
from actors import *

single_move = Sequence(
        name = "Single Move",
        actors = get_list(Actor),
        links = [
            link(case=single_move),
            ],
        sequence_list = [
            message(starts=operator, ends=raspi, message="Hello", categorie="politesse"),
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
        actors = get_list(Actor),
        links = [
            link(case=single_move),
            ],
        sequence_list = [
            message(starts=operator, ends=raspi, message="Hello", categorie='other'),
            activate(actor=operator),
            activate(actor=raspi),
            reponse(starts=raspi, ends=operator, message="Hi there!"),
            message(starts=raspi, ends=raspi, message="Hate him :/"),
            message(starts=raspi, ends=operator, message="Are you ok?"),
            reponse(starts=operator, ends=raspi, message="No, im not"),
            deactivate(actor=operator),
            message(starts=raspi, ends=raspi, message="Fuck Yeah"),
            deactivate(actor=raspi),
            ]
        )

single_move.create()
test.create()
