'''Specifications are stored as a list of dictionaries'''
def spec(**kwargs):
    '''This function converts a functions with kwargs in dictionaries'''
    if not kwargs.get('color'):
        kwargs['color'] = '#lemonchiffon'
    return kwargs

def constrainte(**kwargs):
    '''This function converts a functions with kwargs in dictionaries but adds color in pink'''
    if not kwargs.get('color'):
        kwargs['color'] = '#pink'
    return kwargs
