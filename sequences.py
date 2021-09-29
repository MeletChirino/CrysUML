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
            message(starts=operator, ends=raspi, message="Hello"),
            activate(actor=operator),
            activate(actor=raspi),
            reponse(starts=raspi, ends=operator, message="Hi there!"),
            message(starts=raspi, ends=raspi, message="Hate him :/"),
            message(starts=raspi, ends=operator, message="Are you ok?"),
            reponse(starts=operator, ends=raspi, message="Yes"),
            deactivate(actor=operator),
            message(starts=raspi, ends=raspi, message="Damn it"),
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
            message(starts=operator, ends=raspi, message="Hello"),
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
