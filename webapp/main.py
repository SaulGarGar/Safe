import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
import webapp2
from webapp2_extras import jinja2


class BaseHandler(webapp2.RequestHandler):
    def render_template(self, template_name):d
        renderer = jinja2.get_jinja2(app=app)
        template = renderer.render_template(template_name)
        self.response.write(template)


class LandingHandler(BaseHandler):

    def get(self):
        self.render_template('landing.html')


class MapsHandler(BaseHandler):

    def get(self):
        self.render_template('maps.html')


app = webapp2.WSGIApplication([
    webapp2.Route(r'/',
                  handler=LandingHandler,
                  name='landing_handler',
                  methods=['GET']),

    webapp2.Route(r'/maps',
                  handler=MapsHandler,
                  name='maps_handler',
                  methods=['GET']),
], debug=True)