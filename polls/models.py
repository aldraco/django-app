import datetime

from django.db import models
from django.utils import timezone

# These are the database models for the Polls app
# apps are 'pluggable' and can be used in multiple projects,
# not tied to one installation

# so to make migrations/changes:
# 1) change models here 
# 2) run python manage.py makemigrations to create the migration files
# 3) run python manage.py migrate to apply them to the DB


class Question(models.Model):
  question_text = models.CharField(max_length=200)
  # this field has a human-readable name
  pub_date = models.DateTimeField('date published')
  def __str__(self):
    return self.question_text
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  # improve the display of this output
  # see list_display for more information on method properties
  # define these out at this indent, not within the method
  was_published_recently.admin_order_field = 'pub_date'
  was_published_recently.boolean = True
  was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
  # this is a one-to-many relationship
  question = models.ForeignKey(Question)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  def __str__(self):
    return self.choice_text

