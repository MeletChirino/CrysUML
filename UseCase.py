from crysuml.UseCase import *

client = Actor(name = 'client',)
database = Actor(name='Database', type='database')
cloud = Actor(name="Google", type='cloud')
read = Case(
        name='Read',
        note="jas;ldkfjh;ladksj",
        links=[
            {"actor": client, "type": "simple",},
            {"actor": database, "type": "simple",},
            ]
        )
write = Case(
        name='Mentir',
        note="jas;ldkfjh;ladksj",
        links=[
            {"actor": client, "type": "simple",},
            {"case": read, "type": "include",},
            {"actor": cloud, "type": "simple",},
            ]
        )
delete = Case(
        name = "Delete",
        links = [
            {"actor": database, "type": "simple"},
            {"actor": client, "type": "simple"},
            {"case": write, "type": "extends"},
            ]
        )

use_case_diagram = Diagram(
        cases = [read, write, delete],
        actors = [client, database, cloud]
        )
