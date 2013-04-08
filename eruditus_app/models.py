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

class Post(models.Model):
    user = models.ForeignKey(User)
    publish_date = models.DateTimeField
    
    class Meta:
        abstract = True
        
class PostMeta(models.Model):
    META_TYPE_CHOICES = (
                         ('cat', 'Category'),
                         ('tag', 'Tag'),
                         )
    post = models.ManyToManyField(Post)
    
        
class Text(Post):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    content = models.TextField
    n_comment = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title
    

    
    