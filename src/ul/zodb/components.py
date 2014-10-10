# -*- coding: utf-8 -*-

from cromlech.zodb import PossibleSite
from persistent import Persistent
from ul.content import components
from zope.annotation.interfaces import IAttributeAnnotatable
from zope.location import Location


@implementer(IAttributeAnnotatable)
class Content(components.Content, Persistent):

    def __init__(self, **kwargs):
        Persistent.__init__(self)
        components.Content.__init__(self, **kwargs)


@implementer(IAttributeAnnotatable)
class Container(components.Container, BTreeContainer):

    def __init__(self, **kwargs):
        BTreeContainer.__init__(self)
        components.Container.__init__(self, **kwargs)


class Root(BTreeContainer, PossibleSite, Location):
    pass
