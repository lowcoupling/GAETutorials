from google.appengine.ext import webapp
from google.appengine.api import users
from globalObjects import JINJA_ENVIRONMENT

class MapPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'logout'
            username = user.nickname()
            template_values = {
            'user': username,
            'url': url,
            'url_linktext': url_linktext,
            }
        else:
            url = users.create_login_url(self.request.uri)   
            url_linktext = 'login'
            username='no'     
            template_values = {
            'url': url,
            'url_linktext': url_linktext,
            }
        template = JINJA_ENVIRONMENT.get_template('/templates/mapPage.html')
        self.response.write(template.render(template_values))