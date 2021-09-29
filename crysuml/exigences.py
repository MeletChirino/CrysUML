'''Exigence library'''
class Exigence_():
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = ""
        if kwargs.get('description'): self.name = kwargs['description']
        return {'name': self.name, 'description': self.description,}

def exigence(**kwargs):
        return kwargs
