from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers


schema_view = get_swagger_view(title='Django Starter API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^auth/', include('authentication.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
