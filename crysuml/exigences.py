'''Exigences library'''
class Exigence_():
    def __init__(self, **kwargs):
        '''
        An exigence is a need of your costumer, you must write it short and clear. Keywords are
        name : unique name of your exigence, no spaces
        verbose_name : Name shown in a readable way
        description : description of the exigence
        color : You can color your exigences to differentiate hierarchy in diagram. Color are plantuml colors
        '''
        self.name = kwargs['name']
        self.description = ""
        if kwargs.get('description'): self.name = kwargs['description']
        return {'name': self.name, 'description': self.description,}

def exigence(**kwargs):
    '''This will color  the exigence in standard bussiness yellow color'''
    if not kwargs.get('color'):
        kwargs['color'] = '#lemonchiffon'
    return kwargs

def constrainte(**kwargs):
    '''This will color  the exigence in a danger red color'''
    if not kwargs.get('color'):
        kwargs['color'] = '#pink'
    return kwargs
