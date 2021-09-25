'''General functions for crysuml'''
import gc
import plantuml

def draw_plantuml(file_name):
    try:
        diagram = plantuml.PlantUML(
                url='http://www.plantuml.com/plantuml/img/',
                )
        diagram.processes_file(file_name)
        return diagram
    except Exception as e:
        print(e)


def get_list(class_name):
    trash = gc.get_objects()
    class_list = []
    for obj in trash:
        if isinstance(obj, class_name):
            class_list.append(obj)

    return class_list

def link_type(string):
    switcher = {
            "simple": ["--", ""],
            "include": [".>", ": include"],
            "extends": ["<.", ": extends"],
            }
    return switcher[string]

def check_kwargs(string, kwargs, **default):
    if string in kwargs and kwargs[string]:
        return kwargs[string]
    elif 'default' in default and default['default']:
        return default['default']
    else:
        return ""

def link(**kwargs):
    return kwargs
