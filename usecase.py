from crysuml.functions import get_list
from crysuml.UseCase import Diagram
from cases import *
from actors import *

#this command lists all the cases in cases.py
#if you want to skip any case you can either pop it 
#our from list or do your own list
cases_list = get_list(Case)
#this command lists all the actors in actors.py
actors_list = get_list(Actor)

use_case_diagram = Diagram(
        system_name = "Robot Planteur",
        cases = cases_list,
        actors = actors_list
        )

