#!/usr/bin/env python
# coding: utf-8

import os
import web
from web import form

web.config.debug = True
#web.config.debug = False

urls = (
    '', 'remain',
    '/(.*)/', 'redirect',    
    '/', 'main',
    '/login', 'login',
    '/logout', 'logout'
)

app = web.application(urls, globals())
application = app.wsgifunc()
curr_dir = os.path.dirname(__file__)
web.config.session_parameters['cookie_path'] = '/'

ds = web.session.DiskStore(curr_dir + '/sessions')
#db = web.database(dbn='mysql', db='mysecureweb', user='dev', pw='Intel@123')
#ds = web.session.DBStore(db, 'sessions')
if web.config.get('_session') is None:
    session = web.session.Session( app, ds, initializer={'username':'anonymous', 'loggedin':False} )
    web.config._session = session
else:
    session = web.config._session

render = web.template.render(curr_dir + '/templates/', base='layout', globals={'context': session})

allowed = (
    ('chenric','999'),
)

class redirect:
    def GET(self, path):
        web.seeother('/' + path)

class remain:
    def GET(self):
        web.seeother('/')

class main:
    def GET(self):
        if session.get( 'loggedin', True ):
            return render.main()
        raise web.seeother('/login')
            
class login:
    def GET(self):
        if session.get( 'loggedin', True ):
            raise web.seeother('/')
        else:
            return render.login()

    def POST(self):
        wi = web.input()
        if (wi.username, wi.password) in allowed:
            session.loggedin = True
            session.username = wi.username
            raise web.seeother('/')
        else:
            return render.login()

class logout:
    def GET(self):
        session.kill()
        ds.cleanup(0.002)  
        raise web.seeother('/login')

if __name__ == "__main__":
    app.run()

#END OF FILE
