from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^auth/', include('authentication.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
