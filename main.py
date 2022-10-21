import justpy as jp

from webApp.about import About
from webApp.homepage import Home
from webApp.dictionary import Dictionary
from webApp import page
import inspect

imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and hasattr(obj, 'path'):
            jp.Route(obj.path, obj.serve)
        else:
            pass

#jp.Route(Home.path, Home.serve)
#jp.Route(About.path, About.serve)
#jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port = 8002)

#/dictionary