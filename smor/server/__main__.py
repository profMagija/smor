
from . import serve
import sys

args = {}

for arg in sys.argv[1:]:
    k, v = arg.split('=', 1)
    args[k] = v

serve(**args)