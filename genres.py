import urllib
import webapp2
import jinja2
import os

from unearth import Story
from google.appengine.ext import db
from google.appengine.api import users


JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)


class Comedy(webapp2.RequestHandler):
	
	def get(self):

		query = Story.all()
		query.filter("genre = ", "Comedy")
		query.order("-rating")

		template_values = {
		'query': query	
		}            

		template = JINJA_ENVIRONMENT.get_template('storylist.html')
		self.response.write(template.render(template_values))

class SliceOfLife(webapp2.RequestHandler):

	def get(self):
		query = Story.all()
		query.filter("genre = ", "Slice of Life")
		query.order("-rating")

		template_values = {
		'query': query
		}            

		template = JINJA_ENVIRONMENT.get_template('storylist.html')
		self.response.write(template.render(template_values))


class Romance(webapp2.RequestHandler):

	def get(self):
		query = Story.all()
		query.filter("genre = ", "Romance")
		query.order("-rating")

		template_values = {
		'query': query
		}            

		template = JINJA_ENVIRONMENT.get_template('storylist.html')
		self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([('/genre/comedy', Comedy),
							('/genre/slice-of-life', SliceOfLife),
							('/genre/romance', Romance)],
							debug=True)  