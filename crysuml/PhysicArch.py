"""Components file Library"""
from crysuml.LogicArch import get_categorie_list
from .functions import draw_plantuml

class Component():
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.verbose_name = kwargs['name']
        if kwargs.get('verbose_name'):
            self.verbose_name = kwargs['verbose_name']
        self.ports = kwargs['ports']
        self.categorie = kwargs['categorie']
        if kwargs.get('description'):
            self.description = kwargs['description']

class PhysicalArch():
    def __init__(self, **kwargs):
        self.name = "physical_architecture"
        if kwargs.get('name'):
            self.name = kwargs['name']
        self.components_list = kwargs['components_list']
        sequences_list = kwargs['sequences_list']
        self.categories = get_categorie_list(sequences_list)
        self.connections = kwargs['connections']

    def create_md(self):
        self.diagram()
        create_md(
                name = "Components",
                description = "This file shows the physical architecture of the PC interface",
                instance_list = components_list,
                )

    def diagram(self):
        file_name = F"docs/diagrams/{self.name}_diagram.txt"
        f = open(file_name, "w")
        f.write("@startuml\nleft to right direction\n")
        #write categories
        for categorie in self.categories:
            if not categorie == "default":
                f.write(F"package {categorie} {{\n")
                for component in self.components_list:
                    #import pdb; pdb.set_trace()
                    if component.categorie == categorie:
                        f.write(F"map {component.name} {{\n")
                        for port in component.ports:
                            f.write(F"{port} =>\n")
                        f.write("}\n")
                f.write("}\n")

        for connection in self.connections:
            f.write(F"{connection}")

        f.write("\n@enduml")
        f.close()
        draw_plantuml(file_name)

def port(component, port):
    return F"{component.name}::{port}"

def connect(port1, port2, **kwargs):
    if kwargs.get('bidirectional'):
        if kwargs['bidirectional'] and kwargs.get('message'):
            return F"{port1} <--> {port2} : {kwargs['message']}\n"
        elif kwargs['bidirectional']:
            return F"{port1} <--> {port2}\n"
    if kwargs.get('message'):
        return F"{port1} --> {port2} : {kwargs['message']}\n"
    return F"{port1} --> {port2}\n"

