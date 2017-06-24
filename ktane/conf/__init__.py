import sys


try:
    from .settings import *
except ImportError as e:
    sys.stderr.write("""
ERROR: It looks like settings.py is missing:

    {}

""".format(str(e)))

    sys.exit(1)