
__version__ = '0.1'

# export the API here
from .api import trace, get_current_trace, append_trace, end_current_trace

from .config import configure
from .thread import local  # XXX remove me from here
