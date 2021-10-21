from crysuml.Specifications import *
from crysuml.functions import link
specs_list = [
        spec(
            name = "frontend",
            verbose_name = "Frontend",
            description = "L'interface doit avoir un\nfrontend facile a comprendre\npour l'utilisateur en utilisant Qt",
            links = [
                link(exigence='interface_graphique'),
                link(exigence='code_language'),
                ],
            ),
        spec(
            name = "api",
            verbose_name = "Communication API",
            description="L'interface doit avoir une\nAPI de communication pour\nechanger des donnes ave\nle robot",
            links = [
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
            description = "L'api de communication doit\netre capable d'envoyer\ndes coordonnes relative\nde deplacement pour le\nmovement semi automatique\ndu robot",
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
            description = "L'interface doit etre documente\nen format d'oxygen. Il seront\nutilises git et github comme\noutils de versionage.",
            links = [
                link(exigence='coding_constraint'),
                link(exigence='version_control'),
                ],
            ),
        spec(
            name = 'languange',
            verbose_name = "Language",
            description = "L'interface sera developee\nalexchirino.music@gmail.comen langage python.",
            links = [
                link(exigence='code_language'),
                ],
            ),
        ]
