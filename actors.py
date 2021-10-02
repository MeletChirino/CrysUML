from crysuml.UseCase import Actor

operator = Actor(
        name = 'Operator',
        description = 'Operator is going to say the robot what they should do'
        )
raspi = Actor(
        name='Unite_Centrale',
        verbose_name='Unite centrale',
        description = 'This is going to control the whole stuff',
        type='component'
        )
