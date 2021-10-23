from usecase import *
from exigences import *
from sequences import *
from specs import specs_list
from crysuml.matrix import matrix
from crysuml.functions import create_md
from crysuml.logic_architecture import *
from crysuml.Sequence import Sequence

def main():
    matrix(specs_list, exigences_list, 'exigence', 'Specs V Besoins')
    semi_auto_move.create()
    set_parameters.create()
    receive_data.create()
    manual_mode_seq.create()
    create_md(
            name = "Specifications",
            description = "This file shows specs",
            instance_list = specs_list,
            diagram_name = "specifications",
            footer = "We all agreed 28/sept/2021",
            matrix = (specs_list, exigences_list, 'exigence', 'Specs V Besoins'),
            )
    create_md(
            name = "Exigences",
            description = "This file shows exigences",
            instance_list = exigences_list,
            diagram_name = "exigences",
            footer = "We all agreed 28/sept/2021",
            )
    create_md(
            name = "Cases",
            description = "This file shows cases",
            instance_list = cases_list,
            #diagram_name = "Use Case",
            matrix = (cases_list, exigences_list, 'exigence', 'Cases V Besoins'),
            footer = "We all agreed 28/sept/2021",
            )
    create_md(
            name = "Actors",
            description = "This are the actors of our systems",
            instance_list = actors_list,
            footer = "Those actors are going to do the best for our project"
            )
    use_case_diagram.create()
    matrix(cases_list, exigences_list, 'exigence', 'Cases V Besoins')
    sequences_list = get_list(Sequence)
    logic_architecture_diagram(sequences_list)

    return 0

main()
