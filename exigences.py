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
            description = "L'interface devra recevoir les donnes qui envoie le robot",
            ),
        exigence(
            name = "messages",
            verbose_name = "Commander le robot",
            description = "L'interface devra commander le robot a distance."
            ),
        exigence(
            name = "wireless",
            verbose_name = "Comunication sans fils",
            description = "L'interface devra se comuniquer avec le robot par une signal sans-fil.",
            links = [
                link(exigence="messages", type="extension"),
                link(exigence="receive_info", type="extension"),
                ]
            ),
        exigence(
            name = "real_time",
            verbose_name = "Temps reel",
            description = 'L\'interface doit montrer l\'image en temps reel du robot',
            links = [
                link(exigence="receive_info", type="extension"),
                ]
            ),
        exigence(
            name = "final_report",
            verbose_name = "Montrer l'info",
            description = 'L\'interface doit montrer l\'information acquise par le robot',
            links = [
                link(exigence="receive_info", type="extension"),
                ]
            ),
        ]

