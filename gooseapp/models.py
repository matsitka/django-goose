from django.db import models

#goose
from goose import Goose

#random
from django.contrib.auth.models import UserManager

# Create your models here.
class Post(models.Model):

     created_at = models.DateTimeField(auto_now_add=True)


     def randomString():
        um = UserManager()
        return um.make_random_password(length=10)

     random = models.CharField(max_length=10, default=randomString)

     def __unicode__(self):
        return self.random
        #return unicode(self.created_at)

class Article(Post):

    url = models.URLField(max_length=500, default="")

    def __unicode__(self):
        return self.url
        #return unicode(self.created_at)

    final_url = models.URLField(max_length=500, default="", blank=True)

    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    keywords = models.TextField(blank=True)

    content = models.TextField(blank=True)

    domain = models.CharField(max_length=200, blank=True)

    domain_link = models.TextField(blank=True)

    original_image_url = models.CharField(max_length=500, blank=True)

    favicon_url = models.CharField(max_length=500, blank=True)

    movies = models.CharField(max_length=500, blank=True)



    def download_url(self, url):

        url = self.url
        #g = Goose()
        #g = Goose({'browser_user_agent': 'Mozilla', 'parser_class':'soup'})
        g = Goose({'parser_class':'soup'}) #does this parser works for all?

        article = g.extract(url=url)

        self.title = article.title
        self.description = article.meta_description
        self.keywords = article.meta_keywords

        self.content = article.cleaned_text

        self.domain = article.domain

        self.movies = article.movies


        try:
            self.original_image_url = article.top_image.src
        except AttributeError:
            self.original_image_url = ""

        self.favicon_url = article.meta_favicon

        self.final_url = article.final_url

        #test
        self.domain_link = article.tags


    def save(self, *args, **kwargs):
        self.download_url(self)
        super(Article, self).save(*args, **kwargs)