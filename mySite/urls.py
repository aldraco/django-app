from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mySite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url function takes two argumnets: a regex, and a view, 
    # and two optionals: kwargs and name

    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# above, note there is no 'end of line' regex marker.
# Django takes whatever is left after the match and sends it as a parameter
# to the include() URLconf for the rest of the processing.

#functionality intended to provide 'plug and play' easy addition.