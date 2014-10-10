# -*- coding: utf-8 -*-

import cromlech.zodb
from ul.browser import Publication
from cromlech.zodb import Site, get_site
from cromlech.zodb.middleware import ZODBApp
from cromlech.zodb.utils import init_db
from zope.component.interfaces import ISite, IPossibleSite
from ul.browser.decorators import with_zcml, with_i18n


class ZODBPublication(Publication):
    """Publication mixin
    """

    @classmethod
    @with_zcml('zcml_file')
    @with_i18n('langs', fallback='en')
    def create(cls, gc, session_key='session.key', environ_key='zodb.key',
               conf=None, name='app', root=None):
        if root is None:
            root = cls.root
        db = init_db(conf, make_application(name, root))
        app = cls(session_key, environ_key, name)
        return ZODBApp(app, db, key=environ_key)

    def __init__(self, session_key, environ_key, name):
        self.session_key = session_key
        self.environ_key = environ_key
        self.name = name
        self.publish = self.get_publisher()

    def site_manager(self, environ):
        conn = environ[self.environ_key]
        site = get_site(conn, self.name)
        return Site(site)
