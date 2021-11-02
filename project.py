# package import
from crysuml.matrix import matrix
from crysuml.functions import create_md
from crysuml.LogicArch import *
from crysuml.Sequence import Sequence
from crysuml.PhysicArch import *
# files with info
from exemples.sequences import *
from exemples.components import *
from exemples.usecase import *
from exemples.exigences import *
from exemples.specs import specs_list

def main():
    sequences_list = get_list(Sequence)
    logic_architecture_diagram(sequences_list)
    components_list = get_list(Component)
    Arch = PhysicalArch(
            components_list = components_list,
            sequences_list = sequences_list,
            connections = connections_list
            )
    Arch.diagram()

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

    return 0

main()
