from crysuml.Specifications import *
from crysuml.functions import link
specs_list = [
        spec(
            name = "piloter",
            verbose_name = "Pilotage PC",
            description = "L'interface graphique doit\npiloter le robot à distance\navec un ordinateur disponible\nsur Windows ou Linux.",
            links = [
                link(exigence="piloter"),
                ],
            ),
        spec(#new new
            name = "wireless",
            verbose_name = "Wireless communication",
            description = """
            L’interface graphique
            sur PC communiquera
            directement avec le
            module WiFi sur le
            Raspberry Pi 4 de
            l’unité centrale.
            """,
            links = [
                link(exigence = 'wireless'),
            ],
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
        spec(#new
            name = "api",
            verbose_name = "Communication API",
            description="""Le backend de l'interface
            graphique doit avoir une
            API de communication pour
            échanger des données avec
            le robot.
            """,
            links = [
                link(spec="piloter", type="extension"),
                link(exigence='wireless'),
                link(spec='wireless', type='extension'),
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
        spec(#new
            name='lidar_process',
            verbose_name = 'Lidar Processing',
            description = "L’interface graphique doit être capable de traiter et utiliser l'information du Lidar en moins de 20 seconds.",
            links = [
                link(exigence="functions"),
                ]
            ),
        spec(#new
            name = "lidar_show",
            verbose_name = "Show Lidar",
            description = "L'API doit recevoir des données du Lidar pour créer la cartographie et pour connaitre la position actuelle du robot.",
            links = [
                link(spec='frontend', type="extension"),
                link(spec='lidar_process', type="extension"),
                link(exigence="receive_info"),
                ]
            ),
        spec(#new
            name = 'data_api',
            verbose_name = 'Get Plain Data',
            description = """
            L'interface graphique
            doit recevoir les
            données des capteurs
            et les montrer
            immédiatement sur des
            widgets texte brut.
            """,
            links = [
                link(spec="frontend", type="extension"),
                link(spec="api", type="extension"),
                link(exigence="receive_info"),
                ]
            ),
        spec(#new
            name = "buttons",
            verbose_name = "Buttons mode manuel",
            description = """
            L'interface graphique
            doit avoir des boutons
            pour un pilotage manuel
            du robot. Les fonctions
            de ces boutons seront :
            Avancer, reculer, rotation
            gauche et rotation droite.
            Ces boutons seront désactivés
            tant que le mode semi-
            autonome est actif.
            """,
            links = [
                link(spec="frontend", type="extension"),
                link(spec="api", type="extension"),
                link(exigence="manual_mode"),
                ],
            ),
        spec(#new
            name = 'errors',
            verbose_name = 'Error Handling',
            description = """
            L'interface doit être
            capable de recevoir les
            erreurs du robot et de
            les montrer à l'utilisateur
            immédiatement sur des
            widgets texte brut.""",
            links = [
                link(spec="frontend", type="extension"),
                link(spec="api", type="extension"),
                link(exigence="functions"),
                ],
            ),
        spec(#new
            name = 'select_points',
            verbose_name = 'Points in the map',
            description = '''
            L'interface doit permettre
            à l’utilisateur de
            sélectionner un point
            d'arrivée dans la cartographie
            et de le convertir en une
            coordonnée compréhensible par
            l’unité centrale.
            ''',
            links = [
                link(spec='lidar_process', type="extension"),
                link(spec='frontend', type="extension"),
                link(spec="api", type="extension"),
                ],
            ),
        spec(#new
            name = 'send_coordinates',
            verbose_name = 'Send Coordinates',
            description = """
            L'API de communication
            doit être capable d'envoyer
            des coordonnées de
            déplacement pour le mouvement
            semi-automatique du robot.""",
            links = [

                ],
            ),
        spec(#new
            name = "traject_status",
            verbose_name = 'Etat du trajet',
            description = """
            L'interface graphique doit
            être capable de recevoir
            l’état du trajet en mode
            semi-autonome. Soit le
            trajet est en cours, soit
            il est complet.""",
            links = [
                link(spec='api', type="extension"),
                link(spec='frontend', type="extension"),
                link(spec='errors', type="extension"),
                ]
            ),
        spec(#new
            name = 'set_params',
            verbose_name = "Set Parameters",
            description=" L'interface doit être\ncapable de modifier les\nparamètres de déplacement\ndu robot comme la vitesse\nou l'accélération en\nutilisant des widgets de\nsaisie de texte connectés\nà l’API de communication.",
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
