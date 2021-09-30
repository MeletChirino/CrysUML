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
            footer = "We all agreed 28/sept/2021"
            )
    create_md(
            name = "Cases",
            description = "This file shows cases",
            instance_list = cases_list,
            footer = "We all agreed 28/sept/2021"
            )
    create_md(
            name = "Actors",
            description = "This are the actors of our systems",
            instance_list = actors_list,
            footer = "Those actors are going to do the best for our project"
            )
    #matrix(cases_list, exigences_list, 'exigence')
    return 0

main()
