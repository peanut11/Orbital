import urllib
import webapp2
import jinja2
import os
import datetime

from google.appengine.ext import db
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Story(db.Model):
    title = db.StringProperty()
    author = db.StringProperty(indexed=False)
    url = db.StringProperty(indexed=False)
    genre = db.StringProperty()
    rating = db.StringProperty()
    status = db.StringProperty()
    characters = db.TextProperty(indexed=False)
    description = db.TextProperty(indexed=False)
    editor = db.TextProperty(indexed=False)


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

class MainPageUser(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()

        if user:  # signed in already
            template_values = {
                'nickname': users.get_current_user().nickname(),
                'logout': users.create_logout_url(self.request.host_url),
            }
            template = JINJA_ENVIRONMENT.get_template('genrelogin.html')

            if users.is_current_user_admin():
                template = JINJA_ENVIRONMENT.get_template('addstory.html')
            
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)


    def post(self): 
        self.story = Story(title=self.request.get('title'), 
                    author=self.request.get('author'), 
                    url=self.request.get('link'), 
                    genre=self.request.get('genre'),
                    rating=self.request.get('rating'),
                    characters=self.request.get('characters'),
                    description=self.request.get('desc'),
                    editor=self.request.get('editor')
                    )
        self.story.put()
        self.redirect("/login/")

class AboutUsUser(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            template_values = {
            'nickname': users.get_current_user().nickname(),
            'logout': users.create_logout_url(self.request.host_url),
            }
        
            template = JINJA_ENVIRONMENT.get_template('aboutuslogin.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)

class FaqUser(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            template_values = {
            'nickname': users.get_current_user().nickname(),
            'logout': users.create_logout_url(self.request.host_url),
            }
            
            template = JINJA_ENVIRONMENT.get_template('faqlogin.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)


class GenrePage(webapp2.RequestHandler):
    
    def get(self):

        template = JINJA_ENVIRONMENT.get_template('genre.html')
        self.response.write(template.render())

class GenrePageUser(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            template_values = {
            'nickname': users.get_current_user().nickname(),
            'logout': users.create_logout_url(self.request.host_url),
            }
        
            template = JINJA_ENVIRONMENT.get_template('genrelogin.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)
class StoryList(webapp2.RequestHandler):

    def get(self):
        query = Story.all()
        query.order("-rating")

        template_values = {
        'query': query
        }            

        template = JINJA_ENVIRONMENT.get_template('storylist.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage),
                                ('/aboutus', AboutUs),
                               ('/faq', Faq),
                               ('/genre', GenrePage),
                               ('/storylist', StoryList),
                               ('/login/', MainPageUser),
                                ('/login/aboutus', AboutUsUser),
                                ('/login/faq', FaqUser),
                                ('/login/genre', GenrePageUser)],
                                 debug=True)      
