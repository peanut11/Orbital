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

class SubmitHandler(webapp2.RequestHandler):

	def get(self):
		self.response.write("Wait while we refer you")

	
	def post(self):
		key = self.request.get("k")
		self.redirect('/genre/stories/%s' % key)



class Comedy(webapp2.RequestHandler):
	
	def get(self):

		genre = "Comedy"
		query = Story.all()
		query.filter("genre = ", genre)
		query.order("-rating")

		template_values = {
		'query': query,
		'genre': genre
		}            

		template = JINJA_ENVIRONMENT.get_template('storylist.html')
		self.response.write(template.render(template_values))

	def post(self):
		title = self.request.get("title")

class SliceOfLife(webapp2.RequestHandler):

	def get(self):

		genre = "Slice of Life"
		query = Story.all()
		query.filter("genre = ", genre)
		query.order("-rating")

		template_values = {
		'query': query,
		'genre': genre
		}            

		template = JINJA_ENVIRONMENT.get_template('storylist.html')
		self.response.write(template.render(template_values))


class Romance(webapp2.RequestHandler):

	def get(self):
		genre = "Romance"
		query = Story.all()
		query.filter("genre = ", genre)
		query.order("-rating")

		template_values = {
		'query': query,
		'genre': genre
		}          

		template = JINJA_ENVIRONMENT.get_template('storylist.html')
		self.response.write(template.render(template_values))


class Ratings(webapp2.RequestHandler):

	def get(self):
		query = Story.all()
		query.order("-rating")

		template_values = {
		'query': query,
		'genre': "All"
		}          

		template = JINJA_ENVIRONMENT.get_template('storylist.html')
		self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([('/genre/ratings', Ratings),
									   ('/genre/comedy', Comedy),
									   ('/genre/submit', SubmitHandler),
				 		   			   ('/genre/slice-of-life', SliceOfLife),
								   	   ('/genre/romance', Romance)],
							debug=True)  