""" main package from crysuml"""
from .functions import draw_plantuml, link_type, check_kwargs, link

class Actor():
    def __init__(self, **kwargs):
        """ keywords:
            name, type, description, note
        """
        self.name = kwargs['name']
        if 'type' in kwargs and kwargs['type']: self.type = kwargs['type']
        else: self.type = "actor"

        if kwargs.get('verbose_name'):
            self.verbose_name = kwargs['verbose_name']

        self.description = ""
        if kwargs.get('description'):
            self.description = kwargs['description']
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
        self.name = ""
        if kwargs.get('name'):
            self.name = kwargs['name']
        self.cases = kwargs['cases']
        self.actors = kwargs['actors']
        self.system_name = "System"
        if kwargs.get("system_name"):
            self.system_name = kwargs['system_name']
        #packages

    def create(self):
        #create use case diagram with plantuml
        file_name = "docs/diagrams/use_case_diagram.txt"
        f = open(file_name, "w")
        f.write("@startuml\nleft to right direction\n")
        f.close()
        f = open(file_name, "a")
        print("Creating Use Case diagram")

        for actor in self.actors:
            f.write(F"{actor.type} \"{actor.name}\"\n")

        i = 0
        f.write(F"package \"{self.system_name}\" {{ \n")
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
        draw_plantuml(file_name)

def get_case_u(cases, case_name):
    i=0
    for case in cases:
        if case.name == case_name:
            return F"u{i}"
        i += 1
    pass

