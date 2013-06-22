from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from anotherPage import AnotherPage
from authorizedPage import AuthorizedPage 

class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')

application = webapp.WSGIApplication([
                                      ('/', MainPage),
                                      ('/anotherpage.html',AnotherPage),
                                      ('/auth.html',AuthorizedPage)
                                      ], debug=True)

def main():
    run_wsgi_app(application)
            

if __name__ == "__main__":
    main()
