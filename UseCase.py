from crysuml.UseCase import *

operator = Actor(name = 'operator',)
database = Actor(name='Database', type='database')
robot = Actor(name="Robot", type='component')
configure = Case(
        name = 'Configure',
        links = [
            link(actor=operator, type='simple'),
            link(exigence="configure"),
            link(actor=robot, type='simple'),
            ]
        )
select_use = Case(
        name = 'Select Use',
        description = '''
        User can select mode that robot will behave
        ''',
        links = [
            link(actor=operator, type='simple')
            ]
        )
move = Case(
        name = 'Move Around the house',
        description = '''
        Robot will move around the hous avoiding obstacles
        ''',
        links = [
            link(exigence='move'),
            link(case=select_use, type='extends'),
            link(actor=robot, type='simple'),
            ]
        )
eat = Case(
        name = 'Eat some food',
        description = '''
        The Robot must eat only the amount of food given
        ''',
        links = [
            link(exigence='eat'),
            link(case=select_use, type='extends'),
            link(actor=robot, type='simple'),
            ]
        )
map_house = Case(
        name = 'Map all the house',
        description = 'Robot must save a map of the whole place',
        links = [
            link(case=move, type='extends'),
            link(actor=database, type='simple'),
            link(exigence='map')
            ]
        )
cases_list = [select_use, move, eat, map_house]

use_case_diagram = Diagram(
        cases = cases_list,
        actors = [operator, database, robot]
        )
