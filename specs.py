from crysuml.Specifications import *
from crysuml.functions import link
specs_list = [
        spec(
            name = "piloter",
            verbose_name = "Piloter le robot",
            description = "L'interface doit piloter\nle robot a distance avec\nun ordinateur.",
            ),
        spec(
            name = "frontend",
            verbose_name = "Frontend",
            description = "L'interface doit avoir un\nfrontend facile a comprendre\npour l'utilisateur en utilisant Qt",
            links = [
                link(spec="piloter", type="extension"),
                link(exigence='interface_graphique'),
                link(exigence='code_language'),
                ],
            ),
        spec(
            name = "api",
            verbose_name = "Communication API",
            description="L'interface doit avoir une\nAPI de communication pour\nechanger des donnes ave\nle robot",
            links = [
                link(spec="piloter", type="extension"),
                link(exigence='wireless'),
                link(exigence="receive_info"),
                ],
            ),
        spec(
            name = "lidar_api",
            verbose_name = "LiDar Data",
            description = "L'API doit recevoir des\ndonnes du LiDar",
            links = [
                link(spec="api", type="extension"),
                link(exigence="receive_info"),
                ]
            ),
        spec(
            name='lidar_process',
            verbose_name = 'Lidar Processing',
            description = "Lo'interface doit entre capable\nde processer et manipuler\nl'information du Lidar en\nmoins de 20 seconds",
            links = [
                link(exigence="functions"),
                ]
            ),
        spec(
            name = "lidar_show",
            verbose_name = "Show Lidar",
            description = "Le frontend doit montrer \nl'information du lidar\nde facon comprensible\npour un etre humain",
            links = [
                link(spec='frontend', type="extension"),
                link(spec='lidar_process', type="extension"),
                link(exigence="receive_info"),
                ]
            ),
        spec(
            name = 'data_api',
            verbose_name = 'Get Plain Data',
            description = "L'interface doit recevoir et\nmontrer des donnees\nen text plain comme\nla vitesse ou l'acceleration",
            links = [
                link(spec="frontend", type="extension"),
                link(spec="api", type="extension"),
                link(exigence="receive_info"),
                ]
            ),
        spec(
            name = "buttons",
            verbose_name = "Direction Buttons",
            description = "L'interface doit avoir des\nboutons pour une pilotage\nmanual du robot.\nLes fonctions de ses boutons\nseront :\nAvancer\nReculer\nTourner gauche\nTourner a droite",
            links = [
                link(spec="frontend", type="extension"),
                link(spec="api", type="extension"),
                link(exigence="manual_mode"),
                ],
            ),
        spec(
            name = 'errors',
            verbose_name = 'Error Handling',
            description = "L'interface doit etre capable\nde recevoir les erreurs\ndu robot et de les montrer a\nl'utlisateur",
            links = [
                link(spec="frontend", type="extension"),
                link(spec="api", type="extension"),
                link(exigence="functions"),
                ],
            ),
        spec(
            name = 'select_points',
            verbose_name = 'Points in the map',
            description = 'L\'interface doit etre capable\nde selectioner un point dans\nla representation des donnees\ndu lidar et de le convertir\nen une coordonee relative.',
            links = [
                link(spec='lidar_process', type="extension"),
                link(spec='frontend', type="extension"),
                ],
            ),
        spec(
            name = 'send_coordinates',
            verbose_name = 'Send Coordinates',
            description = "L'api de communication\ndoit etre capable\nd'envoyer des coordonnes\nrelatives de deplacement\npour le movement semi-\nautomatique du robot",
            links = [
                link(spec="api", type="extension"),
                ],
            ),
        spec(
            name = "traject_status",
            verbose_name = 'Traject status',
            description = "L'interface doit nous dire le\nstatus du trajet en mode\nsemiautomatique. Les status\ndisponibles seront :\nMoving\nFinished\nError (si le cas)",
            links = [
                link(spec='api', type="extension"),
                link(spec='frontend', type="extension"),
                link(spec='errors', type="extension"),
                ]
            ),
        spec(
            name = 'set_params',
            verbose_name = "Set Parameters",
            description="L'interface doit etre capable\nde modifier des parametres\nde mouvement du robot comme\nla vitesse ou l'acceleration.",
            links = [
                link(spec='api', type="extension"),
                link(spec='frontend', type="extension"),
                link(spec='data_api', type="extension"),
                link(exigence='settings'),
                ],
            ),
        spec(
            name = 'documentation',
            verbose_name = "Documentation",
            description = "L'interface doit etre\ndocumente en format\nd'oxygen.",
            links = [
                link(spec='rules', type="extension"),
                link(exigence='coding_constraint'),
                ],
            ),
        spec(
            name = 'version_control',
            verbose_name = "Version Control",
            description = "Ils seront utilises git\net github comme\noutils de versionage.",
            links = [
                link(spec='rules', type="extension"),
                link(exigence='version_control'),
                ],
            ),
        spec(
            name = 'languange',
            verbose_name = "Language",
            description = "L'interface sera\ndevelopee en python.",
            links = [
                link(spec='rules', type="extension"),
                link(exigence='code_language'),
                ],
            ),
        spec(
            name = 'rules',
            verbose_name = "Coding rules",
            description = "Le code doit etre\nlisible et suivre des\nregles de developpe-\nment et versionage",
            links = [
                link(exigence='code_language'),
                link(exigence='version_control'),
                link(exigence='coding_constraint'),
                ],
            ),
        ]
