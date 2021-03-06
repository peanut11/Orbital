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

class StoryPage(webapp2.RequestHandler):

    def get(self, post_id):
        user = users.get_current_user()
        if user:  # signed in already
    		key = post_id
    		story = db.get(key)

    		template_values = {
    		'title': story.title,
           	'author': story.author,
            'rating': story.rating,
            'description': story.description,
            'editor': story.editor,
            'status': story.status,
            'link': story.link,
            'characters': story.characters,
            'nickname': users.get_current_user().nickname(),
            'logout': users.create_logout_url(self.request.host_url),
            }
    
    		template = JINJA_ENVIRONMENT.get_template('storypage.html')
    		self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)


app = webapp2.WSGIApplication([('/genre/stories/(.*)', StoryPage)],
                            debug=True) 