from google.appengine.ext import webapp

class AnotherPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Here is another Page!!!')
