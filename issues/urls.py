from django.conf.urls.defaults import patterns, include, url
from django.views.generic import *
from issues.models import Issue
from django.contrib.auth.decorators import login_required

# Uncomment the next two lines to enable the admin:
urlpatterns = patterns('issues.views',
    url(r'^$', 'index'),
    url(r'^new/$', 'new_issue'),
    url(r'^list/$', login_required(
        ListView.as_view(
            queryset = Issue.objects.all(),
        ))),
        
    # url(r'^test/$', redirect_to, { 'url': '/' }),
)
