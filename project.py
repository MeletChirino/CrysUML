from usecase import *
from exigences import *
from crysuml.matrix import matrix
from crysuml.functions import create_md

def main():
    #use_case_diagram.create()
    create_md(
            name = "Exigences",
            description = "This file shows exigences",
            instance_list = exigences_list,
            footer = "I like that girl"
            )
    create_md(
            name = "Cases",
            description = "This file shows cases",
            instance_list = cases_list,
            footer = "I like that girl, shall do el delicioso?"
            )
    #matrix(cases_list, exigences_list, 'exigence')
    return 0

main()
