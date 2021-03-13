import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return timezone.now() >=self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class BlogPost(models.Model):
    BlogTitle = models.CharField(max_length=200)
    BlogBody = models.CharField(max_length=10000)
    PubDate = models.DateTimeField('date published')
    Author = models.CharField(max_length=200)
    Image = models.CharField(max_length=200)
    def __str__(self):
        return self.BlogTitle

class BlogComment(models.Model):
    comment_body = models.CharField(max_length=500)
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=50)

    def __str__(self):
        return self.comment_body

#class for project posts.
class Project(models.Model):
    ProjectName = models.CharField(max_length=200)
    ProjectText = models.CharField(max_length=10000)
    Images = models.CharField(max_length=200) #want to make this a list field eventually, need SQL

    def __str__(self):
        return self.ProjectText
