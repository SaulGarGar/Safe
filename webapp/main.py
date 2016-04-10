import os
import webapp2
from webapp2_extras import jinja2

class BaseHandler(webapp2.RequestHandler):
    def render_template(self, template_name):
        renderer = jinja2.get_jinja2(app=app)
        template = renderer.render_template(template_name)
        self.response.write(template)

class LandingHandler(BaseHandler):

    def get(self):
        self.render_template('landing.html')

class EventsHandler(BaseHandler):
    def get(self):
        self.render_template('events.html')


app = webapp2.WSGIApplication([
    webapp2.Route(r'/',
                  handler=LandingHandler,
                  name='landing_handler',
                  methods=['GET']),

    webapp2.Route(r'/events',
                  handler=EventsHandler,
                  name='events_handler',
                  methods=['GET']),



    ], debug=True)