'''Exigence library'''
class Exigence_():
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.description = ""
        if kwargs.get('description'): self.name = kwargs['description']
        return {'name': self.name, 'description': self.description,}

def exigence(**kwargs):
    if not kwargs.get('color'):
        kwargs['color'] = '#lemonchiffon'
    return kwargs

def constrainte(**kwargs):
    if not kwargs.get('color'):
        kwargs['color'] = '#pink'
    return kwargs
