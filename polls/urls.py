# creating the URL mapping (routes)

from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('', 
      # ex: /polls/
      url(r'^$', views.IndexView.as_view(), name='index'),
      # ex: /polls/4
      url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
      # ex: /polls/4/results
      url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
      # ex: /polls/3/vote/
      url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
      )

# ====== QUESTIONS =======
# HOW TO 
# ... do error handling?

# using capture patterns with regex, and using the ?P<parameter_name>
# defines what that parameter should be called when it is sent to the function
# d+ is of course the regex pattern that will match and be captured.

# The only thing that Django wants is either:
#   1) an HttpResponse
#   2) an exception