import os
import jinja2
import webapp2
import datetime

from google.appengine.ext import db

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Story(db.Model):
	title = db.StringProperty()
	author = db.StringProperty()
	url = db.StringProperty()
	genre = db.StringProperty()
	rating = db.FloatProperty()
	status = db.StringProperty()
	characters = db.TextProperty()
	description = db.TextProperty()
	editor = db.TextProperty()
	date = db.DateTimeProperty()

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
