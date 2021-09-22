from crysuml.UseCase import *

def main():
    client = Actor(name = 'client',)
    database = Actor(name='Database', type='database')
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
                ]
            )
    delete = Case(
            name = "Delete",
            links = [
                {"actor": database, "type": "simple"},
                {"actor": client, "type": "simple"},
                {"case": read, "type": "include"},
                {"case": write, "type": "extends"},
                ]
            )

    diagram = Diagram(
            cases = [read, write, delete],
            actors = [client, database]
            )
    diagram.create()
    return 0

main()


