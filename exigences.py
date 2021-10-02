from crysuml.exigences import exigence

exigences_list = [
        exigence(
            name = "wireless",
            verbose_name = "Comunication sans fils",
            description = "L'interface devra se comuniquer avec le robot par une signal sans-fil."
            ),
        exigence(
            name = "code_language",
            verbose_name = "Langage de programation",
            description = "L'interface devra etre codee en C ou C++."
            ),
        exigence(
            name = "messages",
            verbose_name = "Commander le robot",
            description = "L'interface devra commander le robot a distance."
            ),
        exigence(
            name = "real_time",
            verbose_name = "Temps reel",
            description = 'L\'interface doit montrer l\'image en temps reel du robot'
            ),
        exigence(
            name = "final_report",
            verbose_name = "Montrer l'info",
            description = 'L\'interface doit montrer l\'information acquise par le robot'
            ),
        ]

#generate md file
