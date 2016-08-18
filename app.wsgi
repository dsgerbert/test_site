import sys, os, bottle

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(__file__))

import test_site

application = bottle.default_app()