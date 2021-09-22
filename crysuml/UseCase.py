""" main package from crysuml"""
class Actor():
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.type = check_kwargs('type', kwargs)
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

class Diagram():
    def __init__(self, **kwargs):
        self.cases = kwargs['cases']
        self.actors = kwargs['actors']
        self.system_name = "System"
        #packages

    def create(self):
        #create use case diagram with plantuml
        f = open("diagrams/use_case_diagram.txt", "w")
        f.write("@startuml\n")
        f.close()
        f = open("diagrams/use_case_diagram.txt", "a")
        print("Creating diagram")
        for actor in self.actors:
            f.write(F"actor {actor.name}\n")

        f.write("package System {\n")
        for case in self.cases:
            f.write(F"usecase \"{case.name}\"\n")
        f.write("}\n")
        for case in self.cases:
            for link in case.links:
                start = case.name
                link_ = link_type(link['type'])
                if link.get('actor'):
                    end = link['actor'].name
                else:
                    end = link['case'].name
                f.write(F"{start} {link_[0]} {end} {link_[1]}\n")
        f.write("@enduml")
        f.close()
        return case

def link_type(string):
    switcher = {
            "simple": ["--", ""],
            "include": [".>", ": include"],
            "extends": ["<.", ": extends"],
            }
    return switcher[string]

def check_kwargs(string, kwargs):
    if string in kwargs and kwargs[string]:
        return kwargs[string]
    else:
        return ""

