#! [numpy, defaults]
@numpy_cache()
def greet(name: str, punctuation: str = '!'):
    """Exclaim a greeting

    Implements a caching approach to reduce delay in greeting
    """
    return f'Hello, {name}{punctuation}'


#! [numpy, defaults]


#! [numpy, kwargs]
@numpy_cache(allow_pickle=True)
def greet(name: str, punctuation: str = '!'):
    """Exclaim a greeting

    Implements a caching approach to reduce delay in greeting
    """
    return f'Hello, {name}{punctuation}'


#! [numpy, kwargs]


#! [numpy, functions]
@numpy_cache(load_function=np.loadtxt, save_function=np.savetxt)
def greet(name: str, punctuation: str = '!'):
    """Exclaim a greeting

    Implements a caching approach to reduce delay in greeting
    """
    return f'Hello, {name}{punctuation}'


#! [numpy, functions]
