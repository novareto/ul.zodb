# -*- coding: utf-8 -*-

from .components import Root
from ul.content import events
from cromlech.zodb import LocalSiteManager
from transaction import manager as transaction_manager
from zope.component.interfaces import ISite, IPossibleSite
from zope.event import notify


def make_application(name, model=Root):
    def create_app(db):
        conn = db.open()
        try:
            root = conn.root()
            if not name in root:
                with transaction_manager:
                    app = root[name] = model()
                    if (not ISite.providedBy(app) and
                            IPossibleSite.providedBy(app)):
                        LocalSiteManager(app)
                    notify(events.ApplicationInitializedEvent(app))
        finally:
            conn.close()
    return create_app
