from crysuml.exigences import exigence, constrainte
from crysuml.functions import (create_uml_file, write_file,
        end_file, link, draw_plantuml, class_diagram
        )
"""
Hay que hacer categorias de exigencias tipo:
    importante
    opcional
    critica
    necesaria
    souhaites
    constraintes
    non-fonctionelles
    exigence physique
y asi
"""

exigences_list = [
        exigence(
            name = "settings",
            verbose_name = "Modifier Parametres",
            description = """L'interface graphique devra permettre
de modifier les paramettres du robot
(vitesse, acceleration, etc).""",
            links = [
                link(exigence="interface_graphique", type="extension"),
                ]
            ),
        exigence(
            name = "receive_info",
            verbose_name = "Recevoir information",
            description = """L'interface devra afficher les donnees
des capteurs(vitesse, position)""",
            links = [
                link(exigence="interface_graphique", type="extension"),
                ]
            ),
        exigence(
            name = "manual_mode",
            verbose_name = "Mode Manuel",
            description = """L'Interface permettre d'
envoyer des consignes manuelles de deplacement du robot
(avancer, reculer, rotation gauche, rotation droite)
            """,
            links = [
                link(exigence="interface_graphique", type="extension"),
                ]
            ),
        exigence(
            name = "interface_graphique",
            verbose_name = "Interface graphique",
            description = """Le pilotage du robot devra etre fait
depuis une interface graphique""",
            links = [
                link(exigence="piloter", type="extension"),
                ]
            ),
        exigence(
            name = "piloter",
            verbose_name = "Piloter le robot",
            description = """Le robot devra etre pilote
en distance de facon fonctionel""",
            links = [
                link(exigence="wireless", type="extension"),
                ]
            ),
        exigence(
            name = "functions",
            verbose_name = "Mode Semi-Autonome",
            description = """L’interface PC devra permettre de piloter
de façon semi-autonome le robot.
L’utilisateur définira une position
relative à son point de départ et le
robot devra y aller en toute autonomie
et en évitant les obstacles.""",
            links = [
                link(exigence="interface_graphique", type="extension"),
                ]
            ),
        exigence(
            name = "wireless",
            verbose_name = "Comunication sans fils",
            description = "L'interface devra se comuniquer avec le robot par une signal\nBluetooth ou WiFi.",
            ),
        # ==== Constraintes du developpement ==== #
        constrainte(
            name = "code_language",
            verbose_name = "Langage de programation",
            description = "L'interface graphique devra\netre developpee en python ou Qt.",
            links = [
                link(exigence="interface_graphique", type="extension"),
                ]
            ),
        constrainte(
            name = "coding_constraint",
            verbose_name = "Codage",
            description = """Le code devra être clair,
lisible et compréhensible. Il devra
contenir des commentaires au format
Doxygen permettant la génération
automatique de la documentation.
Les commentaires seront rédigés en
Anglais.""",
            ),
        constrainte(
            name = "version_control",
            verbose_name = "Outil de versionnage",
            description = """Les projets (Software/Hardware) devront
être versionné sur un GitHub public.
Chacun des sous-ensembles logiciels
devront être contenus dans des dépôts
distincts.
Chaque développeur devra être identifié
de manière unique.
Chaque commit devra représenter l’ajout
d’une fonction ou la correction d’un bug
unique.
Un accès suffisant sur les dépôts devra
permettre à OpenIndus de cloner ceux-ci
sur ses outils de versionnage interne.""",
            ),
        ]

