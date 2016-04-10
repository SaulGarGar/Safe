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


class SmsReceive(webapp2.RequestHandler):
    def receive_sms(self):

        from_number = self.RequestHandler.get('From')


        to_number = self.RequestHandler.get('To')


        text = self.RequestHandler.get('Text')

        print 'Text received: %s - From: %s' % (text, from_number)
        return "Text received"

    if __name__ == '__main__':
        app_sms.run(host='0.0.0.0',
                    debug=True)



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