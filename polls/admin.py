from django.contrib import admin

# This is where we tell the admin that objects have an admin interface

from .models import Choice, Question

# this simple line just registers default options iwth the admin panel
# admin.site.register(Question)


# use this way to change the admin options
# this makes the pub date come before the question field
# good thing to think through usability, which fields will come before others
# class QuestionAdmin(admin.ModelAdmin):
  # fields = ['pub_date', 'question_text']

# choice objects are edited on the question admin page.
class ChoiceInline(admin.TabularInline):
  model = Choice 
  extra = 3

# similar to above but with field sets
# create a tuple for each fieldset, and the first element is the title
class QuestionAdmin(admin.ModelAdmin):
  fieldsets= [ 
    (None, {'fields' :
     ['question_text']}),
    ('Date information', 
     {'fields': ['pub_date'],
      'classes': ['collapse']}),
    ]
  inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
