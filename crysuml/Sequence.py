from .functions import draw_plantuml, link_type

class Sequence():
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.links = kwargs['links']
        self.actors = kwargs['sequence']

    def create(self):
        file_name = F'diagrams/{self.name}_sequence.txt'
