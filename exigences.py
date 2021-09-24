from crysuml.exigences import exigence

exigences_list = [
        exigence(
            name = "configure",
            description = "Operator can configure the robot in less than 5 minutes"
            ),
        exigence(
            name = "move",
            description = "Robot must move in any direction"
            ),
        exigence(
            name = "eat",
            description = "Robot must not eat all my food"
            ),
        exigence(
            name = 'map',
            description = 'Robot must create a map of my place'
            )
        ]
