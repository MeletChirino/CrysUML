from crysuml.exigences import exigence
from crysuml.functions import (create_uml_file, write_file,
        end_file, link, draw_plantuml, class_diagram
        )

exigences_list = [
        exigence(
            name = "code_language",
            verbose_name = "Langage de programation",
            description = "L'interface devra etre codee en C ou C++."
            ),
        exigence(
            name = "receive_info",
            verbose_name = "Recevoir information",
            description = "L'interface devra recevoir les donnes de video ou 3D qui\nenvoie le robot",
            ),
        exigence(
            name = "messages",
            verbose_name = "Commander le robot",
            description = "L'interface devra commander les fonctions\n du robot a distance :\n-Faire un Test de connection\n-Scanner toute l'habitation\n-Commander un mouvement d'un point A vers un point B."
            ),
        exigence(
            name = "wireless",
            verbose_name = "Comunication sans fils",
            description = "L'interface devra se comuniquer avec le robot par une signal\nsans-fil.",
            links = [
                link(exigence="messages", type="extension"),
                link(exigence="receive_info", type="extension"),
                ]
            ),
        exigence(
            name = "real_time",
            verbose_name = "Temps reel",
            description = 'L\'interface doit montrer la signal de video en temps reel\ndu robot si l\'operateur le veux',
            links = [
                link(exigence="receive_info", type="extension"),
                ]
            ),
        exigence(
            name = "final_report",
            verbose_name = "Montrer l'info",
            description = 'L\'interface doit montrer l\'information acquise par le robot\n en forme de video, map 3D, ou en forme d\'un petit rapport avec\n les informatinos les plus pertinents',
            links = [
                link(exigence="receive_info", type="extension"),
                ]
            ),
        ]

