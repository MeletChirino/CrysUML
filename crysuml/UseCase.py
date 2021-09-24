""" main package from crysuml"""
import plantuml

class Actor():
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        if 'type' in kwargs and kwargs['type']: self.type = kwargs['type']
        else: self.type = "actor"

        self.note = check_kwargs('note', kwargs)

    def __str__(self):
        return F"ACTOR = {self.name}"

class Case():
    def __init__(self, **kwargs):
        if not(kwargs.get('links')):
            raise Exception('You must set links, if any use links = []')

        self.name = kwargs['name']
        self.description = check_kwargs('description', kwargs)
        self.note = check_kwargs('note', kwargs)
        self.links = kwargs['links']

    def __str__(self):
        return F"USE CASE = {self.name}"

class Package():
    def __init__(self, *args):
        self.list = args

class Diagram():
    def __init__(self, **kwargs):
        self.cases = kwargs['cases']
        self.actors = kwargs['actors']
        self.system_name = "System"
        #packages

    def create(self):
        #create use case diagram with plantuml
        file_name = "diagrams/use_case_diagram.txt"
        f = open(file_name, "w")
        f.write("@startuml\n")
        f.close()
        f = open(file_name, "a")
        print("Creating diagram")

        for actor in self.actors:
            f.write(F"{actor.type} {actor.name}\n")

        i = 0
        f.write("package System {\n")
        for case in self.cases:
            f.write(F"usecase \"{case.name}\" as u{i}\n")
            i += 1

        f.write("}\n")
        for case in self.cases:
            for link in case.links:
                if (link.get('actor') or link.get('case')):
                    start = get_case_u(self.cases, case.name)
                    link_ = link_type(link['type'])
                    if link.get('actor'):
                        end = link['actor'].name
                    else:
                        end = get_case_u(
                                self.cases,
                                link['case'].name
                                )
                    f.write(F"{start} {link_[0]} {end} {link_[1]}\n")
        f.write("@enduml")
        f.close()
        try:
            diagram = plantuml.PlantUML(
                    url='http://www.plantuml.com/plantuml/img/',
                    )
            diagram.processes_file(file_name)
            return diagram
        except Exception as e:
            print(e)

def get_case_u(cases, case_name):
    i=0
    for case in cases:
        if case.name == case_name:
            return F"u{i}"
        i += 1
    pass

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
