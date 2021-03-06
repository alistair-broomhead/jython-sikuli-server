"""
Server-side classes
"""
from jython_sikuli_server.sikuli_class import ServerSikuliClass

try:
    from sikuli import Sikuli
except ImportError, e:
    print e

    class Sikuli(object):
        """ to satisfy sphinx """
        pass


def _get_cls(cls_name):
    #noinspection PyUnresolvedReferences
    class _cls(ServerSikuliClass):
        pass

    try:
        cls = dict(Sikuli.__dict__)[cls_name]
        _cls.__name__ = cls.__name__
        _cls.__doc__ = cls.__doc__
        _cls.__module__ = cls.__module__
    except KeyError, e:
        print e
        _cls.__name__ = cls_name
        _cls.__module__ = "sikuli.Sikuli"
    return _cls


class Vision(ServerSikuliClass):
    """
    Manages interaction with Sikuli's Vision:
        http://doc.sikuli.org/globals.html#Vision.setParameter
    """
    pass

SIKULI_CLASSES = dict()
SIKULI_CLASSES['Vision'] = Vision
SIKULI_CLASSES['App'] = App = _get_cls('App')
SIKULI_CLASSES['Env'] = Env = _get_cls('Env')
SIKULI_CLASSES['Finder'] = Finder = _get_cls('Finder')
SIKULI_CLASSES['Match'] = Match = _get_cls('Match')
SIKULI_CLASSES['Pattern'] = Pattern = _get_cls('Pattern')
SIKULI_CLASSES['Region'] = Region = _get_cls('Region')
SIKULI_CLASSES['Screen'] = Screen = _get_cls('Screen')
SIKULI_CLASSES['Settings'] = Settings = _get_cls('Settings')
SIKULI_CLASSES['SikuliEvent'] = SikuliEvent = _get_cls('SikuliEvent')
del ServerSikuliClass
