'''Specifications library'''
def spec(**kwargs):
    if not kwargs.get('color'):
        kwargs['color'] = '#lemonchiffon'
    return kwargs

def constrainte(**kwargs):
    if not kwargs.get('color'):
        kwargs['color'] = '#pink'
    return kwargs
