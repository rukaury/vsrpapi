from neomodel import (StructuredRel, DateTimeProperty)

class BaseRel(StructuredRel):
    created_on = DateTimeProperty(default_now=True, format='%Y-%m-%d %H:%M')
    updated_on = DateTimeProperty(default_now=True, format='%Y-%m-%d %H:%M')