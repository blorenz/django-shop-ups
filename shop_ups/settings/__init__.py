
try:
    from .local import *
except ImportError, exc:
    exc.args = tuple(
        ['%s (did you rename settings/local-dist.py to settings/local_settings.py?)' % exc.args[0]])
    raise exc
