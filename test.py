from main import *

def main():

    client = Actor(
            type = "human",
            name = "Client",
            note = "This client is an asswhole",
            )
    database = Actor(
            name = "database",
            type = "database",
            note = "This s the amazon server",
            )
    links = [
            {"actor": client, "type": "standard",},
            {"actor": database, "type": "standard",}
            ]
    use_me = UseCase(
            name = "Read",
            description = "Here he reads",
            note = "exemple 1",
            link =[
                {"actor": client, "type": "standard",},
                {"actor": database, "type": "standard",}
                ]
            )
    use_me_now = UseCase(
            name = "Write",
            description = "Here he writes",
            note = "exemple 1",
            link = [
                {"actor": client, "type": "standard",},
                {"use_case": use_me, "type": "include",}
                ]
            )
    use_case = UseCaseDiagram(
            use_case = [use_me, use_me_now],
            notes_on = True
            )
    use_case.create()

main()
