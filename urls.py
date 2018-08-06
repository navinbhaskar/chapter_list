from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns(
    '',
    url(r'/(?P<standard>[a-zA-Z0-9_.-]+)/(?P<subject>[a-zA-Z0-9_.-]+)$', views.chapterlist.as_view(), name = 'chapterlist'),
)