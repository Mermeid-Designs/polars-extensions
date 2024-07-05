#! [pickle]
@pickle_cache
def greet(name: str, punctuation: str = '!'):
    """Exclaim a greeting

    Implements a caching approach to reduce delay in greeting
    """
    return f'Hello, {name}{punctuation}'


#! [pickle]
