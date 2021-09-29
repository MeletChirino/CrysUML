from crysuml.exigences import exigence

exigences_list = [
        exigence(
            name = "wireless",
            description = "L'interface devra se comuniquer avec le robot par une signal sans-fil."
            ),
        exigence(
            name = "code_language",
            description = "L'interface devra etre codee en C ou C++."
            ),
        exigence(
            name = "messages",
            description = "L'interface devra envoyer des messages operationels vers le robot."
            ),
        exigence(
            name = "real_time",
            description = 'L\'interface doit montrer l\'image en temps reel du robot'
            ),
        exigence(
            name = "final_report",
            description = 'L\'interface doit montrer l\'information acquise par le robot'
            ),
        ]
