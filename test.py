import gc
from crysuml.UseCase import *

def main():
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
            name='Write',
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
    another_case = Case(
            name = 'another_case',
            links = [
                2, 4
                ]
            )

    diagram = Diagram(
            cases = [read, write, delete],
            actors = [client, database, cloud]
            )
    diagram.create()
    trash = gc.get_objects()
    for obj in trash:
        if isinstance(obj, Case):
            print(obj)
    return 0

main()


