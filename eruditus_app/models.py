from django.db import models

# Create your models here.

class Site(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name


class User(models.Model):
    sites = models.ManyToManyField(Site)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField
    
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class Term(models.Model):
    TERM_TYPE_CHOICES = (
                         ('cat', 'Category'),
                         ('tag', 'Tag'),
                        )
    term_type = models.CharField(max_length=3, choices=TERM_TYPE_CHOICES)
    term_value = models.CharField(max_length=30)

class License(models.Model):
    short_name = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=50)
    url = models.URLField

# Comments class. Figure it out.

class Post(models.Model):
    user = models.ForeignKey(User)
    publish_date = models.DateTimeField
    n_comment = models.IntegerField(default=0)
    terms = models.ManyToManyField(Term)
    
    class Meta:
        abstract = True
        
class Text(Post):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    content = models.TextField

    def __unicode__(self):
        return self.title
    
class Image(Post):
    title = models.CharField(max_length=500)
    image = models.FileField(upload_to='images')
    license = models.ForeignKey(License)
    source_name = models.CharField(max_length=30)
    source_url = models.URLField
    
class Link(Post):
    link = models.URLField
    link_text = models.CharField(max_length=500)
    description = models.TextField

class Aside(Post):
    title = models.CharField(max_length=500)
    content = models.TextField
    
class Quote(Post):
    quote = models.CharField(max_length=1000)
    by = models.CharField(max_length=30)
    by_url = models.URLField
