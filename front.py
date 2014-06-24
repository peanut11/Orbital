import os
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):

    def get(self):

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

class AboutUs(webapp2.RequestHandler):

	def get(self):

		template = JINJA_ENVIRONMENT.get_template('aboutus.html')
		self.response.write(template.render())

class Faq(webapp2.RequestHandler):

	def get(self):

		template = JINJA_ENVIRONMENT.get_template('faq.html')
		self.response.write(template.render())

application = webapp2.WSGIApplication([('/', MainPage), 
									   ('/aboutus', AboutUs), 
									   ('/faq', Faq)],
									   debug=True)
